import sys
import os
from subprocess import Popen, PIPE


def run_with_modified_rl(args):

    modified_readline_path = os.path.join(os.path.dirname(os.path.realpath('__file__')),
                                          'modified-readline-6.3/shlib')

    if sys.platform == 'darwin':
        os.environ["DYLD_LIBRARY_PATH"] = modified_readline_path
    else:
        os.environ["LD_LIBRARY_PATH"] = ':'.join([modified_readline_path])
        os.environ["LD_PRELOAD"] = '/lib/x86_64-linux-gnu/libtinfo.so.5'

    p = Popen(args)
    p.communicate()

if __name__ == '__main__':
    run_with_modified_rl(sys.argv[1:])
