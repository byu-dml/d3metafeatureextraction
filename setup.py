from setuptools import setup, find_packages

__version__ = "0.1.2"

setup(
    name="d3metafeatureextraction",
    packages = find_packages(exclude=("data",)),
    version = __version__,
    description = "A DARPA D3M wrapper for extracting dataset metafeatures using the byu-dml metalearn package.",
    author = "Roland Laboulaye, Brandon Schoenfeld",
    author_email = "rlaboulaye@gmail.com, bjschoenfeld@gmail.com",
    url = "https://github.com/byu-dml/d3metafeatureextraction",
    keywords = ["metalearning", "metafeature", "machine learning", "metalearn"],
    install_requires = [
        "metalearn==0.2.0",
        "numpy",
        "pandas"
    ],
    dependency_links = [
        "https://gitlab.com/datadrivendiscovery/metadata.git",
        "https://gitlab.com/datadrivendiscovery/primitive-interfaces.git"
    ],
    entry_points = {
        'd3m.primitives' : [
            'd3metafeatureextraction = d3metafeatureextraction:D3MetafeatureExtraction',
        ],
    },
    download_url = "https://github.com/byu-dml/d3metafeatureextraction/archive/{}.tar.gz".format(__version__)
)