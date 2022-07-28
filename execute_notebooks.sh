#!/bin/sh
conda activate prose
cd source/notebooks
jupyter nbconvert --to notebook --execute --inplace tutorials/archival.ipynb
jupyter nbconvert --to notebook --execute --inplace tutorials/catalogs.ipynb
jupyter nbconvert --to notebook --execute --inplace tutorials/fits_manager.ipynb
jupyter nbconvert --to notebook --execute --inplace tutorials/photometry.ipynb
jupyter nbconvert --to notebook --execute --inplace tutorials/reports.ipynb
jupyter nbconvert --to notebook --execute --inplace tutorials/custom_block.ipynb
jupyter nbconvert --to notebook --execute --inplace tutorials/modeling.ipynb

jupyter nbconvert --to notebook --execute --inplace extra.ipynb

cd ../../
