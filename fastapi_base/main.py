from fastapi_base.utils import get_parsed_args
from fastapi_base.app import App
from fastapi_base.project import Project


def main():
    try:
        args, parser = get_parsed_args()
        if args.command:
            if args.command == 'startapp':
                app = App(args.name)
                print(f'[+] App {app.name} created!')
            elif args.command == 'startproject':
                project = Project(args.name)
                print(f'[+] Project \'{project.name}\' created!')
        else:
            parser.print_help()
    except Exception as e:
        print(f"[!] Exception raised, info: '{e}' ")

if __name__ == '__main__':
    main()