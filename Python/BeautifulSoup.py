#! python3

#Beautiful Soap HTML

import requests, bs4

res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(exampleSoup)

elems = exampleSoup.select('#author')
type(elems)

type(elems[0])

str(elems[0])
print(elems[0].getText())

print(elems[0].attrs)
