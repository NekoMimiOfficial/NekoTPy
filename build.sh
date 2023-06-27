#!/bin/bash
# pip3 install build
python3 -m build -n
pip3 uninstall -y NekoTPy
pip3 install dist/*.whl
