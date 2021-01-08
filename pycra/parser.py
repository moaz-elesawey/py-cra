import argparse

def create_parser():

    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, help="django or flask mode")
    parser.add_argument('--app_name', type=str, help='app name if django mode')


    return parser
