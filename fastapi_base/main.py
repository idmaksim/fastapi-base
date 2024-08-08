from fastapi_base.utils import get_parsed_args
from fastapi_base.app import App
from fastapi_base.project import Project
from fastapi_base.crud_app import CRUDApp


def main():
    try:
        args, parser = get_parsed_args()
        if args.command:
            if args.command == 'startapp':
                app = App(args.name)
                print(f'[+] App {args.name} created!')
            elif args.command == 'startcrudapp':
                crud_app = CRUDApp(args.name, args.json_path)
                print(f'[+] CRUD app {args.name} created!')
            elif args.command == 'startproject':
                project = Project(args.name)
                print(f'[+] Project \'{args.name}\' created!')
        else:
            parser.print_help()
    except Exception as e:
        print(f"[!] Exception raised, info: '{e}' ")

if __name__ == '__main__':
    main()