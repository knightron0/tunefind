from bs4 import BeautifulSoup
import requests, getpass
from gmusicapi import Mobileclient


def get_song_id(song):
    try:
        result = api.search(song,10)
    except Exception as e:
        print(e)
        return False
    print(result)
    if len(result['song_hits']) > 0:
        found_song = result['video_hits'][0]
        song_id = found_song['track']['nid']
        return song_id
    else:
        return False


api = Mobileclient()
api.perform_oauth()
api.oauth_login(api.FROM_MAC_ADDRESS)
playlist = api.create_playlist("hiii")
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


ids = []
for i in range(len(allsongs)):
    search_song = "{} - {}".format(allartists[i], allsongs[i])
    song_id = get_song_id(search_song)
    print(song_id)
    if song_id:
        ids.append(song_id)
# print(ids)
# api.add_songs_to_playlist(playlist, ids)