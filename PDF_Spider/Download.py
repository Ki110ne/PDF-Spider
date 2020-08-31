from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import sys
url_lst = []


def download(root):
    html_doc = requests.get(root).content.decode()
    soup = BeautifulSoup(html_doc, 'html.parser')
    links = soup.find_all('a')
    for item in links:
        url = item.get('href')
        if str(url).endswith('.pdf'):
            url_lst.append('/'.join(root.split('/',20)[:-1]) + '/' +url)
        else:
            if '../' in url or '/' not in url:
                break
            new_root = '/'.join(root.split('/',20)[:-1])
            new_url = new_root + '/' + url
            download(new_url)


if __name__ == '__main__':
    download(sys.argv[1])
    for a in url_lst:
        urlretrieve(a,os.path.join('.',str(a).split('/',20)[-1]))





