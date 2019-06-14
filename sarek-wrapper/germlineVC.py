#! /usr/bin/env python
import argparse
import os
import subprocess
import sys

import utils


def parse(argv):
    parser = argparse.ArgumentParser(description="Wrapper for the sarek germlineVC.nf pipeline.")
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-a', '--awsqueue', metavar='AWSQUEUE', type=str, nargs=None,
                               help='the batch queue for the aws executor', required=True)
    required_args.add_argument('-s', '--samples', metavar='SAMPLE', type=str, nargs='+',
                               help='tsv file locations for the samples',
                               required=True)
    required_args.add_argument('-t', '--tools', type=str, nargs=None,
                               help='list of tools to be used by sarek e.g. \'HaplotypeCaller,strelka,mutect2\'',
                               required=True)
    required_args.add_argument('-o', '--outDir', type=str, nargs=None, help='base dir for output delivery',
                               required=True)
    required_args.add_argument('-p', '--profile', type=str, nargs='+', metavar='PROFILE',
                               help='the nextflow profiles you want to use')
    required_args.add_argument('-w', '--work', type=str, nargs=None, help='base dir for work directories',
                               required=True)

    optional_args = parser.add_argument_group('optional arguments')
    optional_args.add_argument('-l', '--logfile', metavar='LOGFILE', dest='logfile', type=str,
                               default='.germlineVC.nextflow.log',
                               nargs=None,
                               help='name for the nextflow logfile in the reports directory, default: .germlineVC.nextflow.log')
    optional_args.add_argument('--reports', metavar='REPORTS', dest='localReportDir', type=str, default='Reports',
                               nargs=None,
                               help='directory where the trace files should be placed. Must NOT be an S3 bucket!')
    optional_args.add_argument('--script_location', metavar='SCRIPT', type=str, default='germlineVC.nf', nargs=None,
                               help='path to the germlineVC.nf script')
    optional_args.add_argument('--genome', type=str, default='GRCh37', nargs=None, help='genome to be used')
    optional_args.add_argument('--genome_base', type=str, default='s3://ngi-igenomes/igenomes/Homo_sapiens/GATK/GRCh37',
                               nargs=None, help='genome location')
    optional_args.add_argument('-d', '--dryrun', action='store_true', help='only show generated commands')
    optional_args.add_argument('-r', '--resume', action='store_true',
                               help='provide if a previous run should be resumed')
    optional_args.add_argument('--nextflow_args', type=str, nargs=None,
                               help='additional arguments directly provided to the workflow provide as string')

    return parser.parse_args(argv)


def run_sample(tsv_file, profile, aws_queue, out_dir, work, script, genome, genome_base, resume, nextflow_args, tools,
               local_report_dir, logfile, dry_run=False):
    nextflow_log = logfile
    command = "nextflow -log %s run %s -profile %s --awsqueue %s --tools %s --sample %s --genome_base %s --genome %s --outDir %s -w %s %s --localReportDir %s --verbose -with-report -with-trace -with-timeline -with-dag -ansi %s" % (
        nextflow_log, script, profile, aws_queue, tools, tsv_file, genome_base, genome, out_dir, work, nextflow_args,
        local_report_dir, resume)
    # remove unnecessary whitespace
    command = ' '.join(command.split())
    utils.log_execution(command, script, local_report_dir)
    retcode = 0
    if not dry_run:
        try:
            subprocess.run(command, shell=True, universal_newlines=True)
        except subprocess.CalledProcessError as err:
            raise RuntimeError('Sarek germlineVC.nf script unsuccessful.') from err
    return


def main(argv):
    args = parse(argv)

    aws_queue = args.awsqueue
    out_base = args.outDir
    work_base = args.work
    script = args.script_location
    genome = args.genome
    genome_base = args.genome_base
    nextflow_args = args.nextflow_args if args.nextflow_args else ''
    tools = args.tools
    local_report_dir = args.localReportDir
    logfile = args.logfile
    dry_run = args.dryrun
    resume = '-resume' if args.resume else ''
    samples = args.samples
    profile = ','.join(args.profile)

    # locate the logfile in the localReportDir
    logfile = os.path.join(local_report_dir, logfile)

    utils.create_report_dir(local_report_dir)

    # if only one sample.tsv given don't change work/out dir
    if len(samples) > 1 and type(samples) == list:
        for sample in samples:
            # create a work and output folder path for each sample
            sample_id = utils.get_simple_basename(sample)
            out_dir = os.path.join(out_base, sample_id)
            work = os.path.join(work_base, sample_id)
            try:
                run_sample(tsv_file=sample, profile=profile, aws_queue=aws_queue, tools=tools, out_dir=out_dir,
                           work=work, script=script, genome=genome, genome_base=genome_base, resume=resume,
                           nextflow_args=nextflow_args, local_report_dir=local_report_dir, dry_run=dry_run,
                           logfile=logfile)
            except RuntimeError as err:
                raise err
    elif len(samples) == 1 and type(samples) == list:

        sample = samples[0]
        out_dir = out_base
        work = work_base
        try:
            run_sample(tsv_file=sample, profile=profile, aws_queue=aws_queue, tools=tools, out_dir=out_dir, work=work,
                       script=script, genome=genome, genome_base=genome_base, resume=resume,
                       nextflow_args=nextflow_args, local_report_dir=local_report_dir, logfile=logfile, dry_run=dry_run)
        except RuntimeError as err:
            raise err
    else:
        sys.stderr.write('Found %i samples. Could not resolve sample: \'%s\'' % (samples, len(samples)))
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
