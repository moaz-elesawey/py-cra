from pycra import PycraDjango
from pycra.parser import create_parser

parser = create_parser()
args = parser.parse_args()
print(args)

if args.app_name:
    PycraDjango(app_name=args.app_name).execute_commands()
else:
    raise ValueError('please enter the app name')
