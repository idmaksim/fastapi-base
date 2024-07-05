import os
import sysconfig


class Project:
    def __init__(self, name: str) -> None:
        if os.path.exists(name):
            raise Exception("Directory already exists")
        
        self.name = name
        self.root_path = f"{self.name}\\"
        self.is_windows = sysconfig.get_platform().startswith('win')
        os.mkdir(self.name)

        self.create_dirs()
        self.create_base_files()
        self.create_venv()
        self.activate_venv()

    def create_dirs(self) -> None:
        dirs = (
            "src",
            "tests",
        )
        for directory in dirs:
            os.mkdir(self.root_path + directory)
            print(f"[+] Directory {directory} created!")

    def create_base_files(self) -> None:
        base_files = (
            "src\\main.py",
            "src\\database.py",
            "src\\models_imports.py",
            ".env",
            "Dockerfile",
            ".gitignore",
            "settings.py",
            "src\\exceptions.py",
            "src\\abstract_service.py",
            "REAMDE.md",
        )
        for base_file in base_files:
            base_file = self.root_path + base_file

            with open(base_file, "w") as file:
                print(f"[+] File {file.name} created!")

    def init_alembic(self) -> None:
        os.system(f'alembic init ./{self.root_path}')

    def create_venv(self) -> None:
        python_cmd = 'python' if self.is_windows else 'python3'

        print('[!] Creating virtual enviroment... Please, wait a few seconds')
        os.system(f'{python_cmd} -m venv {self.root_path}.venv')
        print('[+] Virtual enviroment succesfully created!')

    # TODO: fix venv activation
    def activate_venv(self) -> None:
        activation_path = '.\\' + self.root_path + '.venv\\Scripts\\activate'
        os.system(activation_path)
        print('[+] Venv succesfully activated!')
        os.system('pip freeze') # TODO: remove this
        # self.init_alembic(self.root_path)

    # TODO: write the installing process of all needed libs
    def install_base_libs(self):
        base_libs = (
            'fastapi[all]',
            'sqlalchemy[postgres]',
            'asyncpg',
            'alembic'
        )

        raise NotImplementedError


    
    