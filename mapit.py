# !Python3
'''this program takes command line arguments or (if no arguments given) from
the clipboard and opens a google maps search for that address.'''

import webbrowser
from sys import argv
import pyperclip

if len(argv) > 1:
    #get address from command line
    addr = ''.join(argv[1:])
else:
    addr = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + addr)
