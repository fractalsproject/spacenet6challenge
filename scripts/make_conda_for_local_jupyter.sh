#!/bin/bash

set -e
set -x

INSTNAME="miniconda_for_spacenet6_local_jupyter"
	
MINICONDA="Miniconda3-py37_4.8.2-MacOSX-x86_64.sh"

# Check if we need to install miniconda
if [ ! -d "$HOME/opt/$INSTNAME" ]; then

	# Check if we need to download installer
	if [ -f "/tmp/$MINICONDA" ]; then
		echo "Found miniconda installer"
	else
		echo "Downloading miniconda installer..."
		wget -c "https://repo.anaconda.com/miniconda/$MINICONDA" -O "/tmp/$MINICONDA" 
	fi

	# Run the installer
	chmod +x "/tmp/$MINICONDA"
	bash "/tmp/$MINICONDA" -b -f -p "$HOME/opt/$INSTNAME"

fi

export PATH="$HOME/opt/$INSTNAME/bin:$PATH"

which conda
which pip

conda config --prepend channels conda-forge 
conda config --prepend channels pytorch

tmp_dir=$(mktemp -d)
cd $tmp_dir
pwd
git clone --recursive "https://github.com/fractalsproject/spacenet6challenge.git"
ls -als
cd spacenet6challenge
which conda
echo $PATH
conda env update -f "$tmp_dir/spacenet6challenge/configs/environment.yml"
source "~/opt/$INSTNAME/etc/profile.d/conda.sh"
conda activate base
ls "$tmp_dir/spacenet6challenge"
#pip install -r "$tmp_dir/spacenet6challenge/configs/requirements.txt"
cd solaris
which pip
pip install git+git://github.com/toblerity/shapely.git
echo "$PATH"
pip install .
which conda
pip install jupyter
pip install jupyterlab

python -c "from solaris import utils"

