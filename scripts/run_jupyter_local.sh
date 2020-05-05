#!/bin/bash
 
set -e
set -x

INSTNAME=miniconda_for_spacenet6_local_jupyter

# Check toplevel of repo
if [ ! -d "solaris" ]; then
	echo "Please launch in top level dir of repo."
	exit 1
fi

export PATH="$HOME/opt/$INSTNAME/bin:$PATH"
echo $PATH

which conda
which pip
which python
which jupyter

jupyter lab
