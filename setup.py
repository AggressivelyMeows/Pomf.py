import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pomf",
    version="0.5",
    author="Cerulean",
    author_email="cerulean.connor@gmail.com",
    description="Pomf.se clone uploader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AggressivelyMeows/Pomf.py",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)