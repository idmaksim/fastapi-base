import argparse


def get_parsed_args() -> tuple[argparse.Namespace, argparse.ArgumentParser]:
    args_parser = argparse.ArgumentParser()
    subparsers = args_parser.add_subparsers(dest="command", help="Allowed commands")

    parser_startproject = subparsers.add_parser(
        "startproject", help="Create a new FastAPI project"
    )
    parser_startproject.add_argument(
        "name", type=str, help="The name of the new FastAPI project"
    )

    parser_startapp = subparsers.add_parser("startapp", help="Create a new FastAPI app")
    parser_startapp.add_argument(
        "name", type=str, help="The name of the new FastAPI app"
    )

    args = args_parser.parse_args()
    return args, args_parser

