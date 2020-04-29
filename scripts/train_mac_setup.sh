#!/bin/bash

# I started with a fresh miniconda installation using installer Miniconda3-py37_4.8.2-MacOSX-x86_64.sh.

# Then I basically used the Dockerfile as a script for what to do next.  You will need to fix up some paths here.

source <PATH_TO_MINICONDA>/mininconda3/etc/profile.d/conda.sh
conda config --prepend channels conda-forge 
conda config --prepend channels pytorch
git clone https://github.com/cosmiq/solaris.git
conda env create -f environment.yml
export PATH=/opt/conda/envs/solaris/bin:$PATH
source activate solaris
pip install git+git://github.com/toblerity/shapely.git
cd solaris && pip install .
cd .. && ./train.sh <PATH_TO_SAR_DATA>  # Note, i have a custom train.sh and settings.sh file in this repo

