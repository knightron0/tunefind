from bs4 import BeautifulSoup
import requests, getpass
from gmusicapi import Mobileclient
import importlib
import glob, os
import download
import upload


inpt = input("Do you want to remove all existing .mp3 files? (y/n)")
if(inpt == "y"):
    for file in glob.glob("*.mp3"):
        os.remove(file)

idcurr = 0
show = input("Enter a show: ")
upload.createplist(show)
show.replace(" ", "+")
showurl = "https://www.tunefind.com/show/" + show
page = requests.get(showurl)
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

print("Loading.....")
songs = []
for i in range(len(allsongs)):
    search_song = "{} - {}".format(allartists[i], allsongs[i])
    songs.append(search_song)

songs = set(songs)
for i in songs:
    modified = ""
    for j in i:
        if j == " ":
            modified += "+"
        elif j == "&":
            continue
        elif j == "!":
            continue
        else:
            modified += j
    download.main(modified)

for file in glob.glob("*.mp3"):
    upload.upload(file)
    os.remove(file)
upload.appendtoplaylist()
