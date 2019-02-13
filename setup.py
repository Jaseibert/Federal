import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = (
    ['pandas>=0.19.2', 'pandas-datareader=0.7.0', 're', 'datetime']
)

setuptools.setup(
    name='Federal',
    version='0.1.0',
    author='Jeremy A. Seibert',
    author_email='Jaseibert2@eagles.usi.edu',
    description="A wrapper on to the pandas-datareader package for easier handling of federal reserve (FRED) data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jaseibert/Federal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
