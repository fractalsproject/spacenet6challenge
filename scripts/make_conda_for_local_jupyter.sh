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
#git clone https://github.com/cosmiq/solaris.git
cd spacenet6challenge/solaris
pwd
conda env update --name base -f environment.yml
pip install git+git://github.com/toblerity/shapely.git
pip install .

