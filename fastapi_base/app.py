import os

from fastapi_base.utils import get_samples_path


class App:
    def __init__(self, name: str) -> None:
        if os.path.exists(name):
            raise Exception(f"App with name {name} already exists")
        self.name = name
        self.root_path = f"{self.name}\\"
        os.mkdir(name)
        self.create_files()

    def create_files(self):
        files = (
            'views.py',
            'schemas.py',
            'models.py',
            'dependencies.py',
            'config.py',
            'exceptions.py',
            'service.py',
            'utils.py'
        )
        samples_path = os.path.join(get_samples_path(), 'app')
        for filename in files:
            filename_full = self.root_path + filename
            with open(filename_full, 'w') as file:
                if os.path.exists(os.path.join(samples_path, filename)):
                    with open(os.path.join(samples_path, filename), 'r') as sample:
                        file.write(sample.read())
                print(f'[+] File {file.name} created!')