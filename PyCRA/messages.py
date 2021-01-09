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



# ## npm messages
# class NPM_MESSAGES:
#     NPM_INIT = f'{bcolors.BOLD}{bcolors.OKGREEN}[INFO]{bcolors.ENDC} running{bcolors.OKBLUE} npm init -y{bcolors.ENDC}'
#     NPM_I_BABEL = f'{bcolors.BOLD}{bcolors.OKGREEN}[INFO]{bcolors.ENDC} running{bcolors.OKBLUE} npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev{bcolors.ENDC}'
#     NPM_I_WEBPACK = f'{bcolors.BOLD}{bcolors.OKGREEN}[INFO]{bcolors.ENDC} running{bcolors.OKBLUE} npm i webpack webpack-cli --save-dev{bcolors.ENDC}'
#     NPM_I_REACT = f'{bcolors.BOLD}{bcolors.OKGREEN}[INFO]{bcolors.ENDC} running{bcolors.OKBLUE} npm i react react-dom --save-dev{bcolors.ENDC}'

# # print(NPM_INIT)
# # print(NPM_I_BABEL)
# # print(NPM_I_WEBPACK)
# # print(NPM_I_REACT)

class COMMANDS_MESSAGES:
    @classmethod
    def add_color(cls, command, file_=False):
        if not file_:
            _colored_message = f'{bcolors.BOLD}{bcolors.OKGREEN}[INFO]{bcolors.ENDC} running{bcolors.OKBLUE} {command} {bcolors.ENDC}'
        else:
            _colored_message = f'{bcolors.BOLD}{bcolors.OKGREEN}[INFO]{bcolors.ENDC} running {bcolors.BOLD}{bcolors.OKCYAN} CREATING FILE {bcolors.ENDC} {bcolors.OKBLUE}{command} {bcolors.ENDC}'
        return _colored_message


