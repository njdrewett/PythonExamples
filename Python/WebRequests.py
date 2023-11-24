#Downloading a Webpage with Web requests module

import requests


res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.status_code == requests.codes.ok
print (res.status_code)

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

