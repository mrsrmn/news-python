import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="news-python",
    version="1.0.0",
    author="MakufonSkifto",
    license="GNU General Public License v3.0",
    description="A Python API Wrapper for the https://newsapi.org/ JSON API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MakufonSkifto/news-python",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
