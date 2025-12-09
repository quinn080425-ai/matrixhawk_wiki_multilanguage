#!/bin/bash
set -e

cd common/source/_themes/matrixhawk_sphinx_rtd_theme
git fetch origin
git checkout main
git pull origin main

# 输出子模块最新提交信息
echo "最新子模块提交："
git log -1 --pretty=format:"%h %an %ad %s" --date=iso

cd ../../../..
git add common/source/_themes/matrixhawk_sphinx_rtd_theme
git commit -m "Update matrixhawktheme submodule to latest"

# 输出主项目对子模块的指向
echo "主项目当前指向的子模块 commit："
git submodule status --recursive