#!/usr/bin/env bash

install_dir=$HOME/.local/bin/

mkdir -p $install_dir
chmod +x *.py
cp *.py $install_dir
cd $install_dir
./scraper.py
