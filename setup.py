from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here /'README.md').read_text(encoding="utf-8")


setup (
    name = "scalablewritingpyxel",
    version = "1.3.1",
    description = "A module that give a scalable text writing function for pyxel",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/awing-ding/pyxel_scalable_writing",
    author = "awing-ding",
    email = "awingding.win@gmail.com",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 ",
    ],
    package_dir={'':"src"},
    packages = find_packages(where="src"),
    install_requires = "pyxel",
)