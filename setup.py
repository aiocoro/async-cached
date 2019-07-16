import setuptools


def long_description():
    with open("README.md", "rb") as f:
        long_description = f.read().decode()
    return long_description


setuptools.setup(
    name="async-cached",
    version="3.11.2",
    author="aiocoro",
    author_email="aiocoro@protonmail.ch",
    description="Decorator to cache async function results",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/aiocoro/async-cached",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ),
)
