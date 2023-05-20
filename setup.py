from setuptools import setup, find_packages

# Setup info
with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    # Author
    author="masak1",
    # Version control
    name="aitility",
    version="0.0.3",
    description="AITility is an AI tool for your CLI.",
    long_description=readme,
    license=license,
    # Manifest
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    # Packages
    packages=find_packages(where="aitility"),
    package_dir={"": "aitility"},
    include_package_data=True,
    install_requires=[
        # aitility
        "click",
        "rich",
        "pyxdg",
        "PyYAML",
        # requests
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
)
