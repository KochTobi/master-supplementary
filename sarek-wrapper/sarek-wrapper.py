#! /usr/bin/env python
import argparse
import os
import sys

import annotate as annotate_wrapper
import germlineVC as germlineVC
import main as main_wrapper
import multiQC as multiqc_wrapper
import utils


def parse(argv):
    parser = argparse.ArgumentParser(description="Wrapper for the sarek germline pipeline.")
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-aq_main', '--awsqueue_main', metavar='AWSQUEUE', type=str, nargs=None,
                               help='the batch queue for the aws executor for main.nf', required=True)
    required_args.add_argument('-aq_germ', '--awsqueue_germlineVC', metavar='AWSQUEUE', type=str, nargs=None,
                               help='the batch queue for the aws executor for germlineVC.nf', required=True)
    required_args.add_argument('-aq_an', '--awsqueue_annotate', metavar='AWSQUEUE', type=str, nargs=None,
                               help='the batch queue for the aws executor for annotate.nf', required=True)
    required_args.add_argument('-aq_mqc', '--awsqueue_multiQC', metavar='AWSQUEUE', type=str, nargs=None,
                               help='the batch queue for the aws executor for runMultiQC.nf', required=True)
    required_args.add_argument('-s', '--samples', metavar='SAMPLE', type=str, nargs='+',
                               help='tsv file locations for the samples',
                               required=True)
    required_args.add_argument('-o', '--outDir', type=str, nargs=None, help='base dir for output delivery',
                               required=True)
    required_args.add_argument('-p', '--profile', type=str, nargs='+', metavar='PROFILE',
                               help='the nextflow profiles you want to use', required=True)

    required_args.add_argument('-w', '--work', type=str, nargs=None, help='base dir for work directories',
                               required=True)
    required_args.add_argument('--steps', metavar='STEP', type=str, nargs='+',
                               help='choose from main, germlineVC, annotate, multiQC', required=True)

    optional_args = parser.add_argument_group('optional arguments')
    optional_args.add_argument('--reports', metavar='REPORTS', dest='localReportDir', type=str, default='Reports',
                               nargs=None,
                               help='directory where the trace files should be placed. Must NOT be an S3 bucket!')
    optional_args.add_argument('--script_location', type=str, default='.', nargs=None,
                               help='path to the Sarek directory')
    optional_args.add_argument('--genome', type=str, default='GRCh37', nargs=None, help='genome to be used')
    optional_args.add_argument('--genome_base', type=str, default='s3://ngi-igenomes/igenomes/Homo_sapiens/GATK/GRCh37',
                               nargs=None, help='genome location')
    optional_args.add_argument('-rev', '--revision', type=str, nargs=None,
                               help='The revision if desired and a repository was provided as script location.',
                               default='', required=False)
    optional_args.add_argument('-d', '--dryrun', action='store_true', help='only show generated commands')
    optional_args.add_argument('-r', '--resume', action='store_true',
                               help='provide if a previous run should be resumed')
    optional_args.add_argument('--nextflow_args', type=str, nargs=None, default='',
                               help='additional arguments directly provided to the workflow provide as string')

    return parser.parse_args(argv)


def run_sample(sample, args):
    steps = args.steps
    RUN_MAIN = 'main' in steps
    RUN_GERMLINEVC = 'germlineVC' in steps
    RUN_SOMATICVC = 'somaticVC' in steps and False  # todo implement somaticVC wrapper
    RUN_ANNOTATE = 'annotate' in steps
    RUN_MULTIQC = 'multiQC' in steps

    print('running sample: %s' % sample)
    common_params = []
    sample_id = utils.get_simple_basename(sample)
    work_base = args.work
    out_base = args.outDir
    genome = args.genome
    genome_base = args.genome_base

    dry_run = args.dryrun
    out_dir = os.path.join(out_base, sample_id, 'results')
    resume = args.resume
    work_dir = os.path.join(work_base, sample_id, 'work')
    profile = args.profile
    nextflow_args = "\"%s\"" % args.nextflow_args

    revision = args.revision

    if dry_run:
        common_params.append(['--dryrun'])
    if resume:
        common_params.append(['--resume'])

    profile_params = ['--profile']
    [profile_params.append(p) for p in profile]

    common_params.append(['--outDir', out_dir])
    common_params.append(['--work', work_dir])
    common_params.append(profile_params)
    common_params.append(['--nextflow_args', nextflow_args])
    common_params.append(['--genome', genome])
    common_params.append(['--genome_base', genome_base])

    localReportDir = os.path.join(args.localReportDir, sample_id)

    if RUN_MAIN:
        ## main.nf
        main_params = list(common_params)
        step = 'main'
        # configure custom arguments
        main_queue = args.awsqueue_main
        main_reports = localReportDir + "_%s" % step
        main_script = os.path.join(args.script_location, 'main.nf')
        # take revision into account
        if revision:
            main_script = "" + main_script + " -r %s" % revision
        main_sample = sample
        print("%s %s" % (step, sample))

        main_params.append(['--awsqueue', main_queue])
        main_params.append(['--reports', main_reports])
        main_params.append(['--script_location', main_script])
        main_params.append(['--samples', main_sample])

        main_params = sum(main_params, [])
        # run main.nf
        print("Calling %s with %s" % (main_script, main_params))
        try:
            main_wrapper.main(main_params)
        except RuntimeError as err:
            raise err

    if RUN_GERMLINEVC:
        ## germlineVC.nf
        germlineVC_params = list(common_params)
        step = 'germlineVC'
        # configure custom arguments
        germlineVC_queue = args.awsqueue_germlineVC
        germlineVC_tools = 'HaplotypeCaller,strelka,mutect2'
        germlineVC_reports = localReportDir + "_%s" % step
        germlineVC_script = os.path.join(args.script_location, 'germlineVC.nf')
        # take revision into account
        if revision:
            germlineVC_script = "" + germlineVC_script + " -r %s" % revision
        germlineVC_sample = os.path.join(out_dir, 'Preprocessing/Recalibrated/recalibrated.tsv')

        print("%s %s" % (step, sample))

        germlineVC_params.append(['--awsqueue', germlineVC_queue])
        germlineVC_params.append(['--reports', germlineVC_reports])
        germlineVC_params.append(['--samples', germlineVC_sample])
        germlineVC_params.append(['--script_location', germlineVC_script])
        germlineVC_params.append(['--tools', germlineVC_tools])

        germlineVC_params = sum(germlineVC_params, [])
        # run germlineVC.nf
        print("Calling %s with %s" % (germlineVC_script, germlineVC_params))
        try:
            germlineVC.main(germlineVC_params)
        except RuntimeError as err:
            raise err
    # if RUN_SOMATICVC and False:  # todo implement somaticVC wrapper
    #     ## germlineVC.nf
    #     germlineVC_params = list(common_params)
    #     step = 'germlineVC'
    #     # configure custom arguments
    #     germlineVC_queue = args.awsqueue_germlineVC
    #     germlineVC_tools = 'HaplotypeCaller,strelka,mutect2'
    #     germlineVC_reports = localReportDir + "_%s" % step
    #     germlineVC_script = os.path.join(args.script_location, 'germlineVC.nf')
    #     germlineVC_sample = os.path.join(out_dir, 'Preprocessing/Recalibrated/recalibrated.tsv')
    #     print("%s %s" % (step, sample))
    #
    #     germlineVC_params.append(['--awsqueue', germlineVC_queue])
    #     germlineVC_params.append(['--reports', germlineVC_reports])
    #     germlineVC_params.append(['--samples', germlineVC_sample])
    #     germlineVC_params.append(['--script_location', germlineVC_script])
    #     germlineVC_params.append(['--tools', germlineVC_tools])
    #
    #     germlineVC_params = sum(germlineVC_params, [])
    #     # run germlineVC.nf
    #     print("Calling %s with %s" % (germlineVC_script, germlineVC_params))
    #     germlineVC.main(germlineVC_params)

    if RUN_ANNOTATE:
        ## annotate.nf
        annotate_params = list(common_params)
        step = 'annotate'
        # configure custom arguments
        annotate_queue = args.awsqueue_annotate
        annotate_annTools = 'HaplotypeCaller,Strelka'
        annotate_tools = 'snpeff'
        annotate_reports = localReportDir + "_%s" % step
        annotate_script = os.path.join(args.script_location, 'annotate.nf')
        # take revision into account
        if revision:
            annotate_script = "" + annotate_script + " -r %s" % revision
        print("%s %s" % (step, sample))

        annotate_params.append(['--awsqueue', annotate_queue])
        annotate_params.append(['--reports', annotate_reports])
        annotate_params.append(['--script_location', annotate_script])
        annotate_params.append(['--tools', annotate_tools])
        annotate_params.append(['--annotateTools', annotate_annTools])
        annotate_params = sum(annotate_params, [])
        # run germlineVC.nf
        print("Calling %s with %s" % (annotate_script, annotate_params))
        try:
            annotate_wrapper.main(annotate_params)
        except RuntimeError as err:
            raise err

    if RUN_MULTIQC:
        ## runMultiQC.nf
        multiqc_params = list(common_params)
        step = 'multiQC'
        # configure custom arguments
        multiqc_queue = args.awsqueue_multiQC
        multiqc_reports = localReportDir + "_%s" % step
        multiqc_script = os.path.join(args.script_location, 'runMultiQC.nf')
        print("%s %s" % (step, sample))

        multiqc_params.append(['--awsqueue', multiqc_queue])
        multiqc_params.append(['--reports', multiqc_reports])
        multiqc_params.append(['--script_location', multiqc_script])
        # take revision into account
        if revision:
            multiqc_script = "" + multiqc_script + " -r %s" % revision

        multiqc_params = sum(multiqc_params, [])
        # run germlineVC.nf
        print("Calling %s with %s" % (multiqc_script, multiqc_params))
        multiqc_wrapper.main(multiqc_params)


def main(argv):
    print('main')
    args = parse(argv)
    #    # match input for glob patterns. Should allow for input like *.tsv
    #    samples = [glob.glob(x) for x in args.samples]
    #    # unnest the now double nested list
    #    samples = sum(samples, [])
    samples = args.samples
    print('samples %s' % samples)
    for sample in samples:
        run_sample(sample=sample, args=args)


if __name__ == '__main__':
    main(sys.argv[1:])
