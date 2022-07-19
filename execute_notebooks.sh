#!/bin/sh
conda activate prose
cd source/notebooks
jupyter nbconvert --to notebook --execute tutorials/archival.ipynb
jupyter nbconvert --to notebook --execute tutorials/fitsmanager.ipynb
jupyter nbconvert --to notebook --execute tutorials/photometry.ipynb
jupyter nbconvert --to notebook --execute tutorials/custom_block.ipynb
jupyter nbconvert --to notebook --execute tutorials/modeling.ipynb

jupyter nbconvert --to notebook --execute extra.ipynb

cd ../../
