from PyCRA import PycraDjango, PycraFlask
from PyCRA.parser import create_parser


parser = create_parser()
args = parser.parse_args()

if args.mode:
    if args.mode == 'django':
        if args.app_name:
            PycraDjango(app_name=args.app_name).execute()
        else:
            raise ValueError('please enter the app name')
    elif args.mode == 'flask':
        if args.app_dir:
            PycraFlask(app_dir=args.app_dir).execute()
        else:
            raise ValueError('please enter the app dir')
