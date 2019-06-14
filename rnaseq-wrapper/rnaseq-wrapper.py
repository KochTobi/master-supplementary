import argparse
import os
import sys
import re
import subprocess
import fnmatch

import utils


def parse(argv):
    parser = argparse.ArgumentParser(description="Wrapper for the nf-core/rnaseq pipeline.")

    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--reads', type=str, nargs=1, required=True,
                               help="Reads as string '*_R{1,2}.fastq.gz'")
    required_args.add_argument('--genome', type=str, nargs=1, required=True,
                               help="Name of the desired genome e.g. GRCh37")
    required_args.add_argument('-profile', type=str, nargs='+', required=True, help="Profiles to be used for this run.")

    optional_args = parser.add_argument_group('optional arguments')
    optional_args.add_argument('-d', '--dryrun', action='store_true', help='only generate command')
    optional_args.add_argument('-l', '--logfile', metavar='LOGFILE', dest='logfile', type=str,
                               default=['.nextflow.log'], nargs=1,
                               help='name for the nextflow logfile in the reports directory, default: .nextflow.log')
    optional_args.add_argument('-rev', '--revision', type=str, required=False, default=[], nargs=1,
                               help='Revision of remote repository if a remote repository is given as script.')
    optional_args.add_argument('-s', '--script', metavar='SCRIPT', type=str, nargs=1, required=False,
                               default=['main.nf'],
                               help='Script to be executed. Can be remote repo or local copy')
    optional_args.add_argument('--tracedir', metavar='PATH', type=str, nargs=1, required=False, default=['tracedir'],
                               help='local tracedirectory')
    return parser.parse_known_args(argv)


def getS3Files(s3path):
    # retrieve list of all files in s3 bucket
    files = subprocess.check_output("aws s3 ls %s" % s3path, shell=True)
    files = files.splitlines()
    files = [ filename.split()[3] for filename in files]
    return files


def convertToReadPathsConfig(filesGlob, bucket, outFile='readPaths.config'):
    # get all file and folder names into a list
    files = getS3Files(bucket)
    # construct a regex that matches the glob pattern
    regex = re.compile(fnmatch.translate(filesGlob))
    # filter for files matching the pattern
    matchedFiles = list(filter(regex.search, files))
    # get basename of files and create dictionary
    lines = [ [utils.get_simple_basename(filename), [os.path.join(bucket,filename)]] for filename in matchedFiles]
    readPaths = "readPaths = %s" % lines
    with open(outFile, 'w+') as readPathsConfig:
        readPathsConfig.write("params.%s" % readPaths)
    return outFile

def run(command, script, tracedir, dryrun=False):
    # remove unwanted whitespace
    command = ' '.join(command.split())
    utils.log_execution(command, script, tracedir)
    print("constructed command: %s" % command)
    if not dryrun:
        print("running command: %s" % command)
        os.system('eval %s' % command)
    return


def main(argv):
    # set recommended java heap settings
    os.environ['NXF_OPTS'] = '-Xms1g -Xmx4g'

    args, unknown = parse(argv)

    logfile = os.path.join(args.tracedir[0], args.logfile[0])
    profile = ','.join(args.profile)
    script = args.script[0] if not args.revision else args.script[0] + " -r %s" % args.revision[0]

    reportdir = args.tracedir[0]
    utils.create_report_dir(reportdir)

    reads = args.reads[0]

    command = "nextflow -log %s run %s " % (logfile, script)
    command += "-profile %s --genome %s --tracedir %s " % ( profile, args.genome[0], reportdir)
    # Check for glob files and reads in awsbatch
    if (reads.startswith('s3://')):
        print("Replacing --reads by readPaths")
        s3bucket, globPattern = os.path.split(reads)
        readPathsConfig = convertToReadPathsConfig(filesGlob=globPattern, bucket=s3bucket)
        command += "-c %s " % readPathsConfig
    else:
        command += "--reads %s " % reads

    command += ' '.join(unknown)
    run(command=command, script=script, tracedir=reportdir, dryrun=args.dryrun)


if __name__ == '__main__':
    main(sys.argv[1:])
