"""Setup script for pytrello"""
import os
from setuptools import setup

CWD = os.path.dirname(os.path.abspath(__file__))
VERSION_NS = {}
with open(os.path.join(CWD, 'src', 'trello', '_version.py')) as f:
    exec(f.read(), {}, VERSION_NS)

setup(
    name='pytrello',
    version=VERSION_NS['__version__'],
    packages=[
        'trello', 'trello.models'
    ],
    package_dir={'': 'src'},
    package_data={},
    author='Vincent Moret',
    author_email='moret.vincent@gmail.com',
    url='https://github.com/vmoret/pytrello',
    install_requires=[
        'requests'
    ]
)
