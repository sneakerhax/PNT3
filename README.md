# Python-Network-Tools

This tool is intended to be a modularized set of scripts to perform network functions in Python3.
I found myself having to repeatedly look up how to perform certain Python functions related to networking
so I put them in one place as a reference and functional tool

Note: Tools inside of the scripts folder are stand alone scripts

[![Python 3.7](https://img.shields.io/badge/python-3.7-FADA5E.svg?logo=python)](https://www.python.org/) 
[![Docker](https://img.shields.io/badge/docker-optional-0db7ed.svg?logo=docker)](https://www.docker.com/) [![PEP8](https://img.shields.io/badge/code%20style-pep8-red.svg)](https://www.python.org/dev/peps/pep-0008/) [![License](https://img.shields.io/badge/license-GPL3-lightgrey.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html) [![Twitter](https://img.shields.io/badge/twitter-sneakerhax-38A1F3?logo=twitter)](https://twitter.com/sneakerhax)

## Install

```python3 -m pip install -r requirements.txt```

## Running with Docker (Local build)

```docker build -t pnt3```

Build Docker image (locally)

```docker run -it -v ${PWD}/targets.txt:/targets/targets.txt pnt3 --dnsresolve --target /targets/targets.txt```

Run Docker container with target file

```docker run -it --entrypoint /bin/bash pnt3```

Run Docker container and drop into bash shell to use scripts

## Running with Docker (From Github Container Registry)

```docker run -it -v ${PWD}/targets.txt:/targets/targets.txt ghcr.io/sneakerhax/pnt3:latest --dnsresolve --target /targets/targets.txt```

Run Docker container with target file

```docker run -it --entrypoint /bin/bash ghcr.io/sneakerhax/pnt3:latest```

Run Docker container and drop into bash shell to use scripts
