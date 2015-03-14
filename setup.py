import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="federalist",
    version="0.0.1",
    author="Evan Lane",
    author_email="evanvlane@gmail.com",
    description=("An open-source digital curator of the Federalist Papers."),
    license="GPL",
    keywords="gutenberg reader public domain",
    url="https://github.com/evanvlane/federalist",
    packages=['federalist', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intendeded Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3"],
    )
