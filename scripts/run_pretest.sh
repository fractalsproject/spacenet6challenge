#!/bin/bash

if [ ! -d "$HOME/opt/miniconda_for_spacenet6_local_jupyter" ]; then
	echo "This system is not configured with the right conda environment"
	exit 1
fi

export PATH="$HOME/opt/miniconda_for_spacenet6_local_jupyter/bin:$PATH"
echo $PATH

which conda
which python

source "$HOME/opt/$INSTNAME/etc/profile.d/conda.sh"
conda activate base

testdatapath="../data/test_public/AOI_11_Rotterdam/" $ $1
outputpath="./root" # $2
testdataargs="\
--testdir $testdatapath/SAR-Intensity \
--outputcsv $outputpath \
"

source scripts/settings.sh

CosmiQ_SN6_Baseline/baseline.py --pretest --test $testdataargs $settings

