#! python3
'''
multiClipboard stores the current clipboard as a file that can be recalled
to the clipboard at any time using a keyword commad
'''
import sys
import pyperclip
import shelve
import subprocess
import os
from shutil import rmtree

Usage = ['echo', 'Usage: run from mcb.bat',
    '&', 'echo', 'mcb.bat save [keyword]  - saves current clipboard',
    '&', 'echo', 'mcb.bat rmv [keyword]   - removes clipboard associated with that keyword',
    '&', 'echo', 'mcb.bat rmv all         - removes all clipboard associations',
    '&', 'echo', 'mcb.bat [keyword]       - loads clipboard associated with that keyword',
    '&', 'echo', 'mcb.bat list            - lists saved keywords',
    '&' 'pause']

dataDir = os.path.join('.', 'mcbData')

if os.path.isdir(dataDir) is False:
    os.mkdir(dataDir)

mcbShelf = shelve.open(os.path.join(dataDir,'mcb'))

if len(sys.argv) == 3: 
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()

    elif sys.argv[1].lower() == 'rmv':
        if sys.argv[2].lower() == 'all':
            rmtree(dataDir)
        elif sys.argv[2].lower() in mcbShelf:
            del mcbShelf[sys.argv[2]]
        else:
            subprocess.run(['echo', 'error, key does not exist', '&',
                            'echo', listKeys, '&', 'pause'],
                            shell=True)
elif len(sys.argv) == 2:

    if sys.argv[1].lower() == 'list':
        #calls a cmd window and prints the list of keys
        listKeys = 'current keys: ' + str(list(mcbShelf.keys()))
        subprocess.run(['echo', listKeys,'&', 'pause'],shell=True)
    
    elif sys.argv[1].lower() in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])



else:
    #calls a cmd window and prints the usage of the file
    subprocess.run(Usage,shell=True)

    mcbShelf.close()
