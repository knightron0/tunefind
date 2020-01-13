from bs4 import BeautifulSoup
import requests, getpass
from gmusicapi import Mobileclient
import importlib
import glob, os
import download

idcurr = 0
page = requests.get("https://www.tunefind.com/show/derry-girls")
soup = BeautifulSoup(page.content, 'html.parser')
# EpisodeListItem__links___xftsa 
episodes = soup.select("div.EpisodeListItem__links___xftsa a")
eplinks = []
for i in episodes:
    eplinks.append(i["href"])
eplinks = set(eplinks)
url2 = "https://www.tunefind.com"
allsongs = []
allartists = []
for i in eplinks:
    url = url2 + i
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    sngs = soup.select("div.EpisodeListItem__links___xftsa a")
    sngurls = []
    for j in sngs:
        temp = str(j["href"])
        if temp.count("questions") == 0:
            sngurls.append(url2 + temp)
    for j in sngurls:
        page2 = requests.get(j)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        lol = soup2.select("div.SongList__container___2EXi7 h4.SongTitle__heading___3kxXK a")
        lol2 = soup2.find_all(class_="SongEventRow__subtitle___3Qli4")
        for k in lol2:
            tmp = ""
            for k2 in k:
                tmp += k2.string
            allartists.append(tmp)
        for k in lol:
            allsongs.append(k.text)
print(len(allsongs), len(allartists))


songs = []
for i in range(len(allsongs)):
    search_song = "{} - {}".format(allartists[i], allsongs[i])
    songs.append(search_song)

songs = set(songs)
print(len(songs))
    # download.main(search_song)

os.chdir("/mydir")
for file in glob.glob("*.mp3"):
    print(file)