# About

D3Metafetures wraps the BYU-DML metalearn metafeatures package to fit within the D3M context and
use the D3M dependencies.

# Usage

This package is designed to work inside a D3M docker container.
All of its dependencies can be found within that container.
The docker image python3.6_complete can be found at
registry.datadrivendiscovery.org/jpl/docker_images.

To obtain this image, use:

sudo docker pull registry.datadrivendiscovery.org/jpl/docker_images:python3.6_complete

To create a container from this image, use:

sudo docker run -i -t registry.datadrivendiscovery.org/jpl/docker_images:python3.6_complete /bin/bash
