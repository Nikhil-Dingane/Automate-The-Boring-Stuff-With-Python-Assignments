# download_xkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com'     #starting url
os.makedirs('xkcd', exist_ok=True)      # store comics in ./xkcd
while not url.endswith('#'):
    print ('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')
        print('Downloading image %s...' % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

    image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print ('Done.')
