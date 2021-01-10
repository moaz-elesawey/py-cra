from PyCRA import PycraDjango, PycraFlask
from PyCRA.parser import create_parser
from PyCRA.messages import ERROR_MESSAGE

from PyCRA._checker import _check

import sys


parser = create_parser()
args = parser.parse_args()


_check()

if args.mode:
    if args.mode == 'django':
        if args.app_name:
            try:
                PycraDjango(app_name=args.app_name).execute()
            except Exception as e:
                print(ERROR_MESSAGE.replace('msg', str(e)))
        else:
            print(ERROR_MESSAGE.replace('msg', 'app name is required'))
            sys.exit(0)

    elif args.mode == 'flask':
        if args.app_dir:
            try:
                PycraFlask(app_dir=args.app_dir).execute()
            except Exception as e:
                print(ERROR_MESSAGE.replace('msg', str(e)))
        else:
            print(ERROR_MESSAGE.replace('msg', 'app dir is required'))
            sys.exit(0)
else:
    _mode = str(input('Enter your application mode [django/flask] :- '))
    if _mode == 'django':
        _app_name = str(input('Enter your django app name :- '))
        if _app_name:
            PycraDjango(app_name=_app_name).execute()
        else:
            print(ERROR_MESSAGE.replace('msg', 'app name is required'))
            sys.exit(0)
    elif _mode == 'flask':
        _app_dir = str(input('Enter your app dir :- '))
        if _app_dir:
            PycraFlask(app_dir=_app_dir).execute()
        else:
            print(ERROR_MESSAGE.replace('msg', 'app dir is required'))
            sys.exit(0)
    else:
        print(ERROR_MESSAGE.replace('msg', 'Ivalid set of choices'))
        sys.exit(0)

