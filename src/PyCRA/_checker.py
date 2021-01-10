import os
import sys

from PyCRA.messages import ERROR_MESSAGE

def _check_path():
    _path_dirs = None

    if sys.platform == 'win32':
        _path_dirs = os.environ['PATH'].split(';')
    elif sys.platform == 'linux':
        _path_dirs = os.environ['PATH'].split(':')

    _npm = False
    _node = False

    if _path_dirs:
        for d in _path_dirs:
            if os.path.isfile(d+'/npm'):
                _npm = True

            if os.path.isfile(d+'/node'):
                _node = True

        if _node and _npm:
            return True
        else:
            return False


def _check():

    if not _check_path():
        print(ERROR_MESSAGE.replace('msg', 'please, make sure that npm and nodejs are installed'))
        sys.exit(0)

