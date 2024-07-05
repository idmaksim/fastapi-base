from utils import get_parsed_args
from app import App
from project import Project


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