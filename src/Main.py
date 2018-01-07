import requests # learn more: https://python.org/pypi/requests
from bs4 import BeautifulSoup # learn more: https://python.org/pypi/bs4
import re

name = input("Enter name of Artist: ")
base_url = 'https://www.lyricsondemand.com/' + name[0] + '/' + name + 'lyrics'
total_set = {}

try:
    song_request = requests.get(base_url)
except:
    print('Something when wrong in finding songs belonging to the artist')

all_soup = BeautifulSoup(song_request.text, 'html.parser')
all_lyrics = all_soup.find_all(class_="Highlight")

for i in all_lyrics:
    if not re.search(r'\.\.\/\.\.|#|album', str(i)):
        song_url = 'https://www.lyricsondemand.com/' + name[0] + '/' + name + 'lyrics/' + i.a['href']

        try:
            song_request = requests.get(song_url)
        except:
            print('Something when wrong in finding songs belonging to the artist')

        song_soup = BeautifulSoup(song_request.text, 'html.parser')
        lyrics = song_soup.find(class_="lcontent").text

        n_lyrics = set(re.split('\[.*\]|\n| |, |\(.*\)', lyrics.lower()))
        n_lyrics.pop()

        total_set | n_lyrics

print (len(total_set))