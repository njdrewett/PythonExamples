# OpenSearch Results

import sys
import requests
import bs4

#1. Read the command line arguments from sys.argv.
if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
    print("Search from command line: " + search)


#2. Fetch the search result page with the requests module.
print('Searching...') # display text while downloading the search result page
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q='+ ' '.join(sys.argv[1:]))
res.raise_for_status()
print(res.status_code)

#3. Find the links to each search result.
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(soup)
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')

#4. Call the webbrowser.open() function to open the web browser
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
