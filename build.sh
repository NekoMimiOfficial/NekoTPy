#!/bin/bash

rm ./dist/Neko*
rm ./setup.py
rm ./NekoTPy/__init__.py
pip3 uninstall NekoTPy -y

python3 buildInit.py

# pip3 install build
python3 -m build -n
pip3 install dist/*.whl
