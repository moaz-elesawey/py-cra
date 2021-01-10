import os
import sys

from PyCRA.messages import ERROR_MESSAGE

def _check_path():
    _path_dirs = os.environ['PATH'].split(':')
    _npm = False
    _node = False

    for d in _path_dirs:
        if os.path.isfile(d+'/npm'):
            _npm = True

        if os.path.isfile(d+'/node'):
            _node = True

    print(_node, _npm)
    if _node and _npm:
        return True
    else:
        return False


def _check():

    if not _check_path():
        print(ERROR_MESSAGE.replace('msg', 'please, make sure that npm and nodejs are installed'))
        sys.exit(0)
