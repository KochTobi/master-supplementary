import datetime
import os
import sys


def get_simple_basename(sample):
    if type(sample) == str:
        return os.path.basename(sample).split('.')[0]


def create_report_dir(reportdir):
    # create the localReportDir if not exists
    try:
        # create reports directory
        os.makedirs(reportdir)
    except OSError as err:
        if os.path.isdir(reportdir):
            print('WARNING: Could not create already existing report dir at %s' % reportdir)
            pass
        else:
            raise err


def log_execution(command, script_name, localReportDir):
    log_file = localReportDir
    log_file = os.path.join(log_file, datetime.date.today().isoformat())
    log_file += "-%s-%s" % (str(datetime.datetime.today().hour), str(datetime.datetime.today().minute))
    log_file += "-%s.cmd.sh" % get_simple_basename(script_name)
    with open(log_file, 'a+') as logfile:
        logfile.write('#!/usr/bin/env bash')
        logfile.write(os.linesep)
        logfile.write("# python " + " ".join(sys.argv))
        logfile.write(os.linesep)
        logfile.write(command)
        logfile.write(os.linesep)
