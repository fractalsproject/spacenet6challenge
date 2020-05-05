#!/bin/bash

#GW dstdir=/root
dstdir=./root
model_toplevel=./CosmiQ_SN6_Baseline

settings="\
--rotationfilelocal $dstdir/SAR_orientations.txt \
--maskdir $dstdir/masks \
--sarprocdir $dstdir/sarproc \
--testcsv $dstdir/test.csv \
--yamlpath $dstdir/infer.yaml \
--modeldir $model_toplevel/weights \
--testprocdir $dstdir/sartest \
--testoutdir $dstdir/inference_continuous \
--testbinarydir $dstdir/inference_binary \
--testvectordir $dstdir/inference_vectors \
--rotate \
--mintestsize 80 \
"
