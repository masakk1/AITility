from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    author="masak1",
    name="aitility",
    version="0.0.1",
    description="AITility is an AI tool for your CLI.",
    long_description=readme,
    license=license,
    packages=find_packages(),
    install_requires=[
        "click",
        "rich",
        "click",
        "typing",
        "fake_useragent",
        "pydantic",
        "requests",
        "retrying",
        "tls_client",
    ],
    entry_points={
        "console_scripts": [
            "aitility = aitility.cli:main",
            "ait = aitility.cli:main",
        ],
    },
    # packages=find_packages(exclude=("tests", "docs")),
)
