from setuptools import setup, find_packages
import os


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


def get_version():
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "datasette", "version.py"
    )
    g = {}
    with open(path) as fp:
        exec(fp.read(), g)
    return g["__version__"]


setup(
    name="datasette",
    version=get_version(),
    description="An open source multi-tool for exploring and publishing data",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    license="Apache License, Version 2.0",
    url="https://datasette.io/",
    project_urls={
        "Documentation": "https://docs.datasette.io/en/stable/",
        "Changelog": "https://docs.datasette.io/en/stable/changelog.html",
        "Live demo": "https://latest.datasette.io/",
        "Source code": "https://github.com/simonw/datasette",
        "Issues": "https://github.com/simonw/datasette/issues",
        "CI": "https://github.com/simonw/datasette/actions?query=workflow%3ATest",
    },
    packages=find_packages(exclude=("tests",)),
    package_data={"datasette": ["templates/*.html"]},
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "asgiref>=3.2.10",
        "click>=7.1.1",
        "click-default-group-wheel>=1.2.2",
        "Jinja2>=2.10.3",
        "hupper>=1.9",
        "httpx>=0.20",
        "pint>=0.9",
        "pluggy>=1.0",
        "uvicorn>=0.11",
        "aiofiles>=0.4",
        "janus>=0.6.2",
        "asgi-csrf>=0.9",
        "PyYAML>=5.3",
        "mergedeep>=1.1.1",
        "itsdangerous>=1.1",
        "sqlite-utils>=3.30",
    ],
    entry_points="""
        [console_scripts]
        datasette=datasette.cli:cli
    """,
    setup_requires=["pytest-runner"],
    extras_require={
        "docs": [
            "Sphinx==6.1.3",
            "furo==2022.12.7",
            "sphinx-autobuild",
            "codespell",
            "blacken-docs",
            "sphinx-copybutton",
        ],
        "test": [
            "pytest>=5.2.2",
            "pytest-xdist>=2.2.1",
            "pytest-asyncio>=0.17",
            "beautifulsoup4>=4.8.1",
            "black==22.12.0",
            "blacken-docs==1.12.1",
            "pytest-timeout>=1.4.2",
            "trustme>=0.7",
            "cogapp>=3.3.0",
        ],
        "rich": ["rich"],
    },
    tests_require=["datasette[test]"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Datasette",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Database",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
    ],
)
