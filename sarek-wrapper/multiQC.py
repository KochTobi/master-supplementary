#! /usr/bin/env python
import argparse
import os
import sys

import utils


def parse(argv):
    parser = argparse.ArgumentParser(description="Wrapper for the sarek runMultiQC.nf pipeline.")
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-a', '--awsqueue', metavar='AWSQUEUE', type=str, nargs=None,
                               help='the batch queue for the aws executor', required=True)
    required_args.add_argument('-o', '--outDir', type=str, nargs=None, help='base dir for output delivery',
                               required=True)
    required_args.add_argument('-p', '--profile', type=str, nargs='+', metavar='PROFILE',
                               help='the nextflow profiles you want to use')
    required_args.add_argument('-w', '--work', type=str, nargs=None, help='base dir for work directories',
                               required=True)

    optional_args = parser.add_argument_group('optional arguments')

    optional_args.add_argument('-l', '--logfile', metavar='LOGFILE', dest='logfile', type=str,
                               default='.multiQC.nextflow.log',
                               nargs=None,
                               help='name for the nextflow logfile in the reports directory, default: .nextflow.log')
    optional_args.add_argument('--reports', metavar='REPORTS', dest='localReportDir', type=str, default='Reports',
                               nargs=None,
                               help='directory where the trace files should be placed. Must NOT be an S3 bucket!')
    optional_args.add_argument('--script_location', metavar='SCRIPT', type=str, default='annotate.nf', nargs=None,
                               help='path to the runMultiQC.nf script')
    optional_args.add_argument('--genome', type=str, default='GRCh37', nargs=None, help='genome to be used')
    optional_args.add_argument('--genome_base', type=str, default='s3://ngi-igenomes/igenomes/Homo_sapiens/GATK/GRCh37',
                               nargs=None, help='genome location')
    optional_args.add_argument('-d', '--dryrun', action='store_true', help='only generate commands')
    optional_args.add_argument('-r', '--resume', action='store_true',
                               help='provide if a previous run should be resumed')
    optional_args.add_argument('--nextflow_args', type=str, nargs=None,
                               help='additional arguments directly provided to the workflow, provide as string')

    return parser.parse_args(argv)


def run_multiqc(aws_queue, profile, out_dir, work_dir, script, resume, nextflow_args, local_report_dir, logfile,
                genome, genome_base, dry_run=False):
    nextflow_log = logfile
    command = "nextflow -log %s run %s -profile %s --awsqueue %s --genome %s --genome_base %s --outDir %s -w %s --localReportDir %s %s %s --verbose -with-report -with-trace -with-timeline -with-dag -ansi" % (
        nextflow_log, script, profile, aws_queue, genome, genome_base, out_dir, work_dir, local_report_dir, resume, nextflow_args)
    # remove unnecessary whitespace
    command = ' '.join(command.split())
    utils.log_execution(command, script, local_report_dir)
    if not dry_run:
        os.system('eval %s' % command)
    return


def main(argv):
    args = parse(argv)

    aws_queue = args.awsqueue
    out_dir = args.outDir
    work = args.work
    script = args.script_location
    nextflow_args = args.nextflow_args if args.nextflow_args else ''
    local_report_dir = args.localReportDir
    logfile = args.logfile
    dry_run = args.dryrun
    resume = '-resume' if args.resume else ''
    profile = ','.join(args.profile)
    genome = args.genome
    genome_base = args.genome_base

    # locate the logfile in the localReportDir
    logfile = os.path.join(local_report_dir, logfile)

    utils.create_report_dir(local_report_dir)

    run_multiqc(aws_queue=aws_queue, profile=profile, out_dir=out_dir, work_dir=work, script=script, resume=resume,
                nextflow_args=nextflow_args, local_report_dir=local_report_dir, logfile=logfile, genome=genome,
                genome_base=genome_base, dry_run=dry_run)


if __name__ == '__main__':
    print(sys.argv)
    main(sys.argv[1:])
