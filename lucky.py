# !Python3
# takes command arguments and opens the search resualts of the top 5 links.

import sys
import requests
import bs4
import webbrowser
import logging
logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

print('Googling...')
req = requests.get('https://www.google.ca/search?q=' + ' '.join(sys.argv[1:]))
req.raise_for_status()

#retireve top search resu#lt links
souped = bs4.BeautifulSoup(req.text, 'html.parser')
links = souped.select('.r a')
logging.debug(len(links))
logging.debug(links[0].getText())
assert isinstance(links, list)

#open a browser tab for each result
numOpen = min(5, len(links))
for i in range(numOpen):
    webbrowser.open_new_tab('https://google.com' + links[i].get('href'))
