#!/bin/bash

set -e
set -x

INSTNAME="miniconda_for_spacenet6_local_jupyter"

if [ ! -d "$HOME/opt/$INSTNAME" ]; then
	echo "This system is not configured with the right conda environment"
	exit 1
fi

export PATH="$HOME/opt/miniconda_for_spacenet6_local_jupyter/bin:$PATH"
echo $PATH

which conda
which python

source "$HOME/opt/$INSTNAME/etc/profile.d/conda.sh"
conda activate base


