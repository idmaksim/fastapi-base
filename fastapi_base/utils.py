import os
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
    
    parser_startcrudapp = subparsers.add_parser("startcrudapp", help="Create a new FastAPI CRUD app")
    parser_startcrudapp.add_argument(
        "name", type=str, help="The name of the new FastAPI crud app"
    )
    parser_startcrudapp.add_argument(
        "json_path", type=str, help ="The name of the input json file with schema"
    )
    

    args = args_parser.parse_args()
    return args, args_parser


def get_samples_path() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    samples_dir = os.path.join(current_dir, 'samples')
    return samples_dir

