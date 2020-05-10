# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from io import open
from pretty_format_json import *

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

gh_repo = "https://github.com/weaming/pretty-format-json"

setup(
    name="pretty-format-json",  # Required
    version=version,  # Required
    description="Pretty print json contains python style coments, string literal.",  # Required
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url=gh_repo,  # Optional
    author="weaming",  # Optional
    author_email="garden.yuen@gmail.com",  # Optional
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    keywords="json format",  # Optional
    install_requires=[
        "oyaml",
        "data-process>=0.3.*"
    ],  # Optional
    entry_points={  # Optional
        "console_scripts": [
            "pretty_format_json=pretty_format_json.format:main",
            "yaml_json=pretty_format_json.yaml_json:main",
            "csv_json=pretty_format_json.csv_json:main",
        ]
    },
    project_urls={"Bug Reports": gh_repo, "Source": gh_repo},  # Optional
)
