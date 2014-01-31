
from setuptools import setup, find_packages
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

# Read the version number from a source file.
# Code taken from pip's setup.py
def find_version(*file_paths):
    with open(os.path.join(here, *file_paths), 'r') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name="pwravg",
    version = find_version('pwravg', '__init__.py'),
    description = "Average calculator tool for PWr students",

#    url = 'http://github.com/robin92/pwravg',

    author = 'Rafal Bolanowski',
    author_email = 'robin92pl@gmail.com',

    license = 'MIT',

    classifiers = [
        'Development Status :: 4 - Beta',

        'Environment :: Console',
        
        'Intended Audience :: Education'
        'Intended Audience :: End Users/Desktop',

        'Topic :: Education',

        'License :: OSI Approved',
        'License :: OSI Approved :: MIT License',

        'Natural Language :: Polish',
        
        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords = 'pwr average courses',

    # Requirements
    install_requires = [
        "beautifulsoup4>=4.3.2",
    ],

    packages = find_packages(exclude = ["tests*"]),

#    entry_points = {
#        'console_scripts': [
#            'sample=sample:main',
#        ],
#    },
)

