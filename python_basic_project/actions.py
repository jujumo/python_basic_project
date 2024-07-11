from python_basic_project import shovel
import configargparse
import yaml


def do_bad():
    parser = configargparse.ArgParser(
        config_file_parser_class=configargparse.YAMLConfigFileParser
    )
    parser.add('-c', '--config', required=False, is_config_file=True, help='config file path')
    parser.add_argument("--complains", type=str, default="")
    args = parser.parse_args()
    shovel.dig(args.complains)


if __name__ == '__main__':
    do_bad()
