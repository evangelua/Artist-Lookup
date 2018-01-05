import requests # learn more: https://python.org/pypi/requests
from bs4 import BeautifulSoup # learn more: https://python.org/pypi/bs4
import re

base_url = 'https://genius.com/Eminem-believe-lyrics'
r = requests.get(base_url)

soup = BeautifulSoup(r.text, 'html.parser')
lyrics = str(soup.find(class_="lyrics").text)

n_lyrics = set(re.split('\[.*\]|\n| |, ', lyrics.lower()))
n_lyrics.pop()

print (len(n_lyrics))