#! python3
'''
multiClipboard stores the current clipboard as a file that can be recalled
to the clipboard at any time using a keyword commad
'''
import sys
import pyperclip
import shelve
import subprocess

Usage = '''Usage: run from mcb.bat\n
mcb.bat save [keyword]  - saves current clipboard\n
mcb.bat rmv [keyword]   - removes clipboard associated with that keyword\n
mcb.bat rmv all         - removes all clipboard associations\n
mcb.bat [keyword]       - loads clipboard associated with that keyword\n
mcb.bat list            - lists saved keywords'''

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 3 and sys.argv[1].lower == 'rmv':
    if sys.argv[2].lower == 'all':
        mcbShelf = None
    else:
        try:
            del sys.argv[2]
        except:
            ['error, key does not exist']
    continue

elif len(sys.argv) == 2 and sys.argv[1].lower == 'list':
    #calls a cmd window and prints the list for you
    listKeys = 'current keys:\n' + str(list(mcbShelf.keys()))
    #TODO
    subprocess.run(['echo', listKeys,'&', 'pause'])

else:
    #calls a cmd window and prints the usage of the file for you
    subprocess.run(['echo', Usage, '&' 'pause'])


mcbShelf.close()