#!/usr/bin/python2.7
# encoding: utf-8
'''
generateJiraCodeReport -- generate JIRA-code traceability report

generateJiraCodeReport is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2018 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated

refs
- https://stackoverflow.com/questions/34931386/how-do-i-keep-the-json-key-order-fixed-with-python-3-json-dumps

'''

import sys
import os
import json

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

import readJira
import readStructure
from SvnLogParser import SvnLogParser
from IssuesToCodeRTMGenerator import IssuesToCodeRTMGenerator

__all__ = []
__version__ = 0.1
__date__ = '2018-02-10'
__updated__ = '2018-02-10'

DEBUG = 0
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by user_name on %s.
  Copyright 2018 organization_name. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser     
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("--jira", dest="jiraxml", help="jira issues xml file")
        parser.add_argument("--structure", dest="strcsv", help="jira structure CSV file")
        parser.add_argument("--svnlog", dest="svnlogxml", help="svn xml log file")
        parser.add_argument("--leaftype", dest='leafType', help="deepest JIRA issue type of the report")
        parser.add_argument('-V', '--version', action='version', version=program_version_message)

        # Process arguments
        args = parser.parse_args()

        
        # load jira xml
        with open(args.jiraxml) as f:
            issues=readJira.readJiraXml(f)
    
        # load structure
        with open(args.strcsv) as f:
            structure=readStructure.readStructureCSV(f)

        # add subtasks to structure
        readJira.extendStructureWithSubtasks(structure, issues)
        
        # load svn log
        with open(args.svnlogxml) as f:
            svnlog=SvnLogParser().parse(f)
        
        generator=IssuesToCodeRTMGenerator(structure, issues, svnlog)
        report = generator.generate(args.leafType)
        
        sys.stdout.write("var data = ")
        json.dump(report, sys.stdout, indent=2, sort_keys=True)

        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
#     except Exception, e:
#         if DEBUG or TESTRUN:
#             raise(e)
#         indent = len(program_name) * " "
#         sys.stderr.write(program_name + ": " + repr(e) + "\n")
#         sys.stderr.write(indent + "  for help use --help")
#         return 2

if __name__ == "__main__":
    if DEBUG:
        # debug settings
        pass
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'generateJiraCodeReport_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())