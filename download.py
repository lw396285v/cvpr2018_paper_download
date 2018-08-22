import requests
from pyquery import PyQuery as pyq
import os

if not os.path.exists('papers'):
    os.mkdir('papers')

url_base = "http://openaccess.thecvf.com/%s"

src = pyq(url=url_base % '/CVPR2018.py')('#content')('dl').eq(0).children()

for i in range(0, src.length, 3):
    paper_name = src.eq(i)('a').html()
    download_url = url_base % src.eq(i+2)('a').eq(0).attr('href')
    print('Downloading paper #%d: %s' % (i/3+1, src.eq(i)('a').html()))

    r = requests.get(download_url)
    with open("papers/%s.pdf" % paper_name.replace('/', '\\'), 'wb') as f:
        f.write(r.content)
