from setuptools import setup

setup(
    name='fastapi-base',
    version='2.11',
    entry_points={
        'console_scripts': [
            'fastapi-base = fastapi_base.main:main',
        ],
    },
    install_requires=[
    ],
    author='Dementev Maksim',
    author_email='i@dmaksim.ru',
    description='FastAPI project structure generator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/idmaksim/fastapi-base',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
