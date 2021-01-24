import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="financialmodelingprep",
    version="0.0.1",
    author="Joseph Cottingham | Joseph Conigliari",
    description="The unofficial python interface for the financialmodelingprep API",
    license='MIT',
    author_email="joseph.cottingham@protonmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JosephCottingham/financialmodelingprep-python.git",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests>=2.23.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
