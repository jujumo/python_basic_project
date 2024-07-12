from python_basic_project import shovel
from jsonargparse import ArgumentParser, ActionConfigFile


def do_bad():
    parser = ArgumentParser()
    parser.add_argument('--complains.bad', type=str, default='grr !')
    parser.add_argument('-c', '--config', action=ActionConfigFile, help='config file path')
    config = parser.parse_args()

    shovel.dig(config.complains.bad)


if __name__ == '__main__':
    do_bad()
