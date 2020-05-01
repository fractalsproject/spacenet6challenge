#!/bin/bash

if [ ! -d "spacenet6challenge" ]; 
	then git clone --recursive "https://github.com/fractalsproject/spacenet6challenge.git" ; 
else 
	echo "spacenet6challenge directory already exists"; 
fi


