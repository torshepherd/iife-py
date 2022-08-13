import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

print("Found: ", find_packages())

# This call to setup() does all the work
setup(
    name="iife",
    version="0.1.0",
    description="Bringing the fun of immediately-invoked function expressions to Python!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/torshepherd/iife-python",
    author="Tor Shepherd",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["colored"]
)
