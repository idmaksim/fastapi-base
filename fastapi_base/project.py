import os
import venv
import subprocess
import sys

from fastapi_base.utils import get_samples_path


class Project:
    def __init__(self, name: str) -> None:
        if os.path.exists(name):
            raise Exception("Directory already exists")
        
        self.name = name
        self.root_path = self.name + '\\'
        self.is_windows = sys.platform.startswith('win')
        self.venv_path = os.path.join(self.root_path, '.venv')
        self.venv_python = os.path.join(self.venv_path, 'Scripts', 'python.exe') if self.is_windows else os.path.join(self.venv_path, 'bin', 'python')

        os.mkdir(self.name)

        self.create_dirs()
        self.create_base_files()
        self.create_venv()
        self.install_base_libs()
        self.create_requirements_txt()
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
            'src/abstract_repository.py',
            "README.md",
            'Dockerfile'
        )
        
        samples_path = os.path.join(get_samples_path(), 'project')
        for filename in base_files:
            filename_full = self.root_path + filename
            with open(filename_full, 'w') as file:
                
                print(os.path.exists(os.path.join(samples_path, filename)))
                print(os.path.join(samples_path, filename))
                
                if os.path.exists(os.path.join(samples_path, filename)):
                    with open(os.path.join(samples_path, filename), 'r') as sample:
                        file.write(sample.read())
                print(f'[+] File {file.name} created!')

    def init_alembic(self) -> None:
        os.chdir(self.root_path)    
        subprocess.check_call(['alembic', 'init', 'alembic'])
        os.chdir('../')    

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
            'aiosqlite[sqlalchemy]',
            'uvicorn',
        )
        for lib in base_libs:
            subprocess.check_call([self.venv_python, '-m', 'pip', 'install', lib])
        print('[+] Base libraries successfully installed!')

    def create_requirements_txt(self):
        os.system(f'{self.venv_python} -m pip freeze > {self.root_path}/requirements.txt')