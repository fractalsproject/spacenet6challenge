#!/bin/bash

# set -x # uncomment for verbose logging of commands - useful for debugging
set -e

echo

# Check to see if prereq has already run sucessfully
set +e
python -c "from solaris import utils" > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
	echo '"solaris" package is present.'
	exit 0
fi
set -e

# Install some linux packages
echo "Updating several linux packages..."
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:ubuntugis/ppa && apt-get -y update
sudo apt-get install -y libspatialindex-dev python-rtree gdal-bin
sudo apt-get install -y build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev
sudo apt-get install -y libgdal-dev
sudo gdal-config --version
echo "OK."
echo

# Check conda
echo "Checking conda..."
set +e
gotconda=`which conda`
set -e
if [ -z $gotconda ]; then
	echo "Did not find conda.  Downloading and installing miniconda..."
	wget -c https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
	chmod +x Anaconda3-2019.10-Linux-x86_64.sh
	bash ./Anaconda3-2019.10-Linux-x86_64.sh -b -f -p /usr/local
	gotconda=`which conda`
	if [ -z $gotconda ]; then
		echo "Error: Failed to install miniconda"
		exit 1
	fi
fi
conda config --prepend channels conda-forge
conda config --prepend channels pytorch
echo "OK."
echo

# Clone the project
#echo "Building and installing the solaris project..."
#if [ -d /content/spacenet6challenge ]; then
#	echo 'Cleaning up previous project clone...'
#	rm -r /content/spacenet6challenge 
#fi
#git clone --recursive https://github.com/fractalsproject/spacenet6challenge

# Cleanup any previous env
#if [ -d /usr/local/envs/solaris ]; then
#	echo 'Cleaning up previous conda env...'
#	conda env remove --name solaris
#	echo 'OK.'
#	echo
#fi

echo "Installing solaris environment and package..."
cp /content/spacenet6challenge/solaris_setup_adj.py /content/spacenet6challenge/solaris/setup.py

#cd /content/spacenet6challenge/solaris && conda env create -f environment.yml
#export PATH=/opt/conda/envs/solaris/bin:$PATH
#source activate solaris

cd /content/spacenet6challenge && conda env update -f solaris_environment_adj.yml
export PATH=/opt/conda/bin

#pip install git+git://github.com/toblerity/shapely.git
pip install git+https://github.com/Toblerity/shapely.git@master#egg=shapely-1.7.1dev

cd /content/spacenet6challenge/solaris && pip install .
echo "OK."
echo

echo "Colab prereq finished."
echo
exit 0
