import os, requests
from bs4 import BeautifulSoup
 
def main(query):
    url = "https://www.youtube.com/results?search_query=" + query
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    