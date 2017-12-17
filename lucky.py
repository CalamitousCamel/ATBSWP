#!Python3

import sys
import requests
import bs4
import webbrowser
import logging
#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

print('Googling...')
req = requests.get('https://www.google.ca/search?q=' + ' '.join(sys.argv[1:]))
req.raise_for_status()

#TODO retireve top search resu
#lt links
souped = bs4.BeautifulSoup(req.text, 'html.parser')
links = souped.select('.r a')
logging.debug(len(links))
logging.debug(links[0].getText())
assert type(links) is list

#TODO open a browser tab for each result
numOpen = min(3, len(links))
for i in range(numOpen):
    webbrowser.open_new_tab('https://google.com' + links[i].get('href'))