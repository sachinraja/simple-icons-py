from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requires = f.read().splitlines()

setup(
    name="simpleicons",
    version="4.4.0.4",
    author="Sachin Raja",
    author_email="sachinraja2349@gmail.com",
    license="MIT",
    description="Use a wide-range of icons derived from the simple-icons/simple-icons repo in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xCloudzx/simpleicons",
    packages=find_packages(),
    install_requires=requires,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
