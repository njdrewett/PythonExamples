#!python3

# downloadXkcd.py - Downloads every single XKCD comic

import requests, os, bs4

#1. Download pages with the requests module.
url = 'https://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd
while not url.endswith('#'):
#2. Find the URL of the comic image for a page using Beautiful Soup.
    print('Downloading page %s....' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
#3. Download and save the comic image to the hard drive with iter_content().
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else :
        comicUrl = 'https:' + comicElem[0].get('src')
        # download the image
        print('Downloading image %s'% comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # get the Prev button's URL
    #4. Find the URL of the Previous Comic link, and repeat
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')


print('Done.')


