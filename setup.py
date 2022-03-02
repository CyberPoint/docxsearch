import os
import setuptools

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(__file__) )
PARENT_DIRECTORY = os.path.dirname(CURRENT_DIRECTORY)
VERSION_FILE = "VERSION"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = "0.0.1"
with open( VERSION_FILE, 'r', encoding="utf-8" ) as reader:
    version = reader.read().rstrip().lstrip()

setuptools.setup(
    name="cato-cli", 
    version=version,
    author="CyberPoint International",
    author_email="opensource@cyberpointllc.com",
    description="Provides tool to search docx files for forensic intelligence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://cyberpoint.com",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=['requests_toolbelt','pandas', 'paramiko', 'python-docx'],
    scripts=['scripts/docxsearch'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
