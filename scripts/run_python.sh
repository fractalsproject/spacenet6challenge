#!/bin/bash

set -e
set -x

INSTNAME="miniconda_for_spacenet6_local_jupyter"

PATH_TO_TEST_DATA="/root/Projects/fractalsproject/data/test_public/AOI_11_Rotterdam/"

if [ ! -d "$HOME/opt/$INSTNAME" ]; then
	echo "This system is not configured with the right conda environment"
	exit 1
fi

#if [ ! -d "$PATH_TO_TEST_DATA" ]; then
#	echo "Could not find test data."
#	exit 1
#fi

export PATH="$HOME/opt/miniconda_for_spacenet6_local_jupyter/bin:$PATH"
echo $PATH

which conda
which python

source "$HOME/opt/$INSTNAME/etc/profile.d/conda.sh"
conda activate base

PYTHONPATH='./solaris' python
