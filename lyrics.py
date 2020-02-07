import requests as req
from bs4 import BeautifulSoup

url = 'https://genius.com/Nicki-minaj-yikes-lyrics'

def create_soup(url):
    resp = req.get(url)
    soup = BeautifulSoup(resp.content, 'lxml')
    return soup
