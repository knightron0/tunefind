import os, requests
from bs4 import BeautifulSoup
import youtube_dl

download_options = {
	'format': 'bestaudio/best',
	'outtmpl': '%(title)s.%(ext)s',
	'nocheckcertificate': True,
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}

def geturl(query):
    url = "https://www.youtube.com/results?search_query=" + query
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    divs = soup.select("div.yt-lockup-content h3 a")
    if len(divs) == 0:
        print("Couldn't find song.")
        return False
    finurl = "https://www.youtube.com" + divs[0]["href"]
    return finurl

def main(query):
    with youtube_dl.YoutubeDL(download_options) as dl:
        urls = geturl(query)
        if urls != False:
            dl.download([urls])