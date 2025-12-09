#!/bin/bash
set -e

cd common/source/_themes/matrixhawk_sphinx_rtd_theme
git fetch origin
git checkout main
git pull origin main
cd ../../../..
git add common/source/_themes/matrixhawk_sphinx_rtd_theme
git commit -m "Update matrixhawktheme submodule to latest"