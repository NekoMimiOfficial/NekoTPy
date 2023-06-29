import os
import requests
import json
import asyncio
from NekoTPy import Commands

"""
     ^ ^    NekoTPy telegram bot API wrapper         v Bliss(A)
    =UwU=   this software is distributed as is without warranty
     w w    developed by @NekoMimiOfficial 2023(c) NekoLabs LTD

     NekoTPy is a telegram bot API wrapper which is async ready
     and feature rich to write bots in a more elegant and simple
     style minimizing keystrokes

     this library takes inspiration of the discord.py syntax
     if you are used to it then you'll be at home since its
     almost a 1to1 syntax (minus that it's telegram)

     for more info and guides, please refer to the docs at:
     <DOCS_PLACEHOLDER>
"""

__ntpy_error_list = []

def write(data:str, file:str) -> int:
    """
    a write function to be used internally
    however as the naming convention implies
    it may be used by the user if they wish

    write(data, file)
    accepts 2 positional arguments of type str
    data: the data needed to be written (str)
    file: the file to write to (str)

    yields an int:
    0 on success
    1 on failure

    errors get appended to __ntpy_error_list
    """
    
    try:
        buffer = open(file,'w')
        buffer.write(data)
        buffer.close()
        return 0
    except Exception as e:
        __ntpy_error_list.append(f"Write error@{file}: {e}")
        return 1

def read(file:str) -> str:
    """
    a read function to be used internally
    however as the naming convention implies
    it may be used by the user if they wish

    read(file)
    accepts 1 positional argument of type str
    file: the file to write to (str)

    yields str data:
    expected file contents on success
    expected 'Read error!' on failure

    errors get appended to __ntpy_error_list
    """
    
    try:
        buffer = open(file, 'r')
        contents = buffer.read()
        buffer.close()
        return contents
    except Exception as e:
        __ntpy_error_list.append(f"Read error@{file}: {e}")
        return "Read error!"

def _nhc_parser(file:str):
    """
    to be only used by the ntpy library
    an argument parser for .nhc files known as Neko Hybrid Config files

    nhc file structure:

    ARG1=UwU=ARG2...
    in this case ntpy's nhc file only contains 2 args
    """
    data = read(file)
    data = data.split("=UwU=", 1)
    if len(data) != 2:
        __ntpy_error_list.append(f"Error reading nhc file:{file} check format")
        return 0, 0

    #messages in telegram have an update ID
    #basically each UID is always bigger than the previous pne 
    #and can be used to track the order of messages

    #guid is the global UID or what the app has stored
    #so if it crashes or restarts it remembers the last message
    _guid = data[0]

    #this is a new feature, an interaction ID
    #copies the same principle of the GUID however its
    #only advanced once an interaction has occured
    _giid = data[1]

    return _guid, _giid

class Bot:
    def __init__(self) -> None:
        return None
