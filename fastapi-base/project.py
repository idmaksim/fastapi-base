import os
import venv
import subprocess
import sys


class Project:
    def __init__(self, name: str) -> None:
        if os.path.exists(name):
            raise Exception("Directory already exists")
        
        self.name = name
        self.root_path = os.path.join(self.name)
        self.is_windows = sys.platform.startswith('win')
        self.venv_path = os.path.join(self.root_path, '.venv')
        self.venv_python = os.path.join(self.venv_path, 'Scripts', 'python.exe') if self.is_windows else os.path.join(self.venv_path, 'bin', 'python')

        os.mkdir(self.name)

        self.create_dirs()
        self.create_base_files()
        self.create_venv()
        self.install_base_libs()
        self.init_alembic()

    def create_dirs(self) -> None:
        dirs = (
            "src",
            "tests",
        )
        for directory in dirs:
            os.mkdir(os.path.join(self.root_path, directory))
            print(f"[+] Directory {directory} created!")

    def create_base_files(self) -> None:
        base_files = (
            "src/main.py",
            "src/database.py",
            "src/models_imports.py",
            ".env",
            "Dockerfile",
            ".gitignore",
            "src/settings.py",
            "src/exceptions.py",
            "src/abstract_repository.py",
            "README.md",
        )
        for base_file in base_files:
            base_file_path = os.path.join(self.root_path, base_file)
            with open(base_file_path, "w") as file:
                print(f"[+] File {file.name} created!")

    def init_alembic(self) -> None:
        os.chdir(self.root_path)  # Change directory to the project root
        subprocess.check_call(['alembic', 'init', './alembic'])
        os.chdir('..')  

    def create_venv(self) -> None:
        print('[!] Creating virtual environment... Please, wait a few seconds')
        venv.create(self.venv_path, with_pip=True)
    
        print('[+] Virtual environment successfully created!')

    def install_base_libs(self):
        base_libs = (
            'fastapi[all]',
            'sqlalchemy',
            'asyncpg',
            'alembic',
        )
        for lib in base_libs:
            subprocess.check_call([self.venv_python, '-m', 'pip', 'install', lib])
        print('[+] Base libraries successfully installed!')