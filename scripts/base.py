#!/usr/bin/env python
"""
SYNOPSIS

    TODO helloworld [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    TODO This describes how to use this script. This docstring
    will be printed by the script if there is an error or
    if the user requests help (-h or --help).

EXAMPLES

    TODO: Show some examples of how to use this script.

AUTHOR

    Oliver Hofmanne <ohofmann@hsph.harvard.edu>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.

VERSION

    $Id$
"""
from __future__ import absolute_imports, division, print_function
import logging, optparse, os, time, traceback, sys
#from pexpect import run, spawn

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def main ():
    global options, args
    # TODO: Do something more interesting here...
    pass

if __name__ == '__main__':
    try:
        startTime = time.time()
        p = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(),
                                  usage=globals()['__doc__'], version='$Id$')
        p.add_option('-v', '--verbose', action='store_true',
                     default=False, help='Verbose output')
        p.add_option('-h', '--help', action='store_true',
                     default=False, help='About this script')
        (options, args) = parser.parse_args()

        #if len(args) < 1:
        #    parser.error ('missing argument')

        if options.verbose:
            logging.setLevel(logging.DEBUG)
            logging.debug(time.asctime())
            logging.debug('Debugging mode on')

        if options.help:
            print __doc__
            sys.exit(0)

        main()

        if options.verbose:
            logging.debug(time.asctime())
            logging.debug('Total time in minutes: %s' % ((time.time() -
                                                          startTime) / 60.0))
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        logging.error('Exiting\n%s' % (e))
        traceback.print_exc()
        os._exit(1)
