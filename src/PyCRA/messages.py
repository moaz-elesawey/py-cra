class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class COMMANDS_MESSAGES:
    @classmethod
    def add_color(cls, command, file_=False):
        if not file_:
            _colored_message = f'{bcolors.BOLD}{bcolors.OKGREEN}[INFO]{bcolors.ENDC} running{bcolors.OKBLUE} {command} {bcolors.ENDC}'
        else:
            _colored_message = f'{bcolors.BOLD}{bcolors.OKGREEN}[INFO]{bcolors.ENDC} running {bcolors.BOLD}{bcolors.OKCYAN} CREATING FILE {bcolors.ENDC} {bcolors.OKBLUE}{command} {bcolors.ENDC}'
        return _colored_message

ERROR_MESSAGE = f'{bcolors.FAIL}{bcolors.BOLD}[ERROR] msg {bcolors.ENDC}'
