import os


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
            'constants.py', # this may be deleted
            'exceptions.py',
            'service.py',
            'utils.py'
        )
        samples_path = 'fastapi-base/samples/app/'
        for filename in files:
            filename_full = self.root_path + filename
            with open(filename_full, 'w') as file:
                if os.path.exists(samples_path + filename):
                    with open(samples_path + filename, 'r') as sample_file:
                        sample_code =  sample_file.read()
                        file.write(sample_code)
                print(f'[+] File {file.name} created!')