from setuptools import setup, find_packages
import pathlib


setup (
    name = "scalablewritingpyxel",
    version = "1.1.6",
    description = "A module that give a scalable text writing function for pyxel",
    long_description = "A module that give a scalable text writing function for pyxel, see README.md on github for documentation",
    url = "https://github.com/awing-ding/pyxel_scalable_writing",
    author = "awing-ding",
    email = "awingding.win@gmail.com",
    classifiers = [
        "Development Status :: 5 - Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 ",
    ],
    packages = find_packages(where="src"),
    ressource_requires = "pyxel",

)