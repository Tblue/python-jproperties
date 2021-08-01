import codecs
import os
from setuptools import setup

setup(
    name="jproperties",
    use_scm_version=True,
    description="Java Property file parser and writer for Python",
    # Read the long description from our README.rst file, as UTF-8.
    long_description=codecs.open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "README.rst"
            ),
            "rb",
            "utf-8"
        ).read(),
    author="Tilman Blumenbach",
    author_email="tilman+pypi@ax86.net",
    entry_points={
        "console_scripts": [
            "propconv = jproperties:main"
        ]
    },
    url="https://github.com/Tblue/python-jproperties",
    py_modules=["jproperties"],
    install_requires=["six ~= 1.13"],
    setup_requires=[
        "setuptools_scm ~= 3.3"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development"
    ],
    license="BSD 3-Clause License; partially licensed under the Python Software Foundation License",
    keywords="java property properties file parser reader writer",
)
