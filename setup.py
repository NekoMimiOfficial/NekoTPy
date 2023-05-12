import setuptools
import NekoTPy

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NekoTPy",
    version=NekoTPy.__version__,
    author="NekoMimi",
    author_email="nekomimi@tilde.team",
    description="Telegram API wrapper written in python with command wrapper and context style commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NekoMimiOfficial/NekoTPy",
    project_urls={
        "Bug Tracker": "https://github.com/NekoMimiOfficial/NekoTPy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache2 License",
        "Operating System :: OS Independent",
    ],
    package_dir={"./": "NekoTPy/"},
    install_requires = ['requsts'],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
