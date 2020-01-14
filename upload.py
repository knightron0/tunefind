from gmusicapi import Mobileclient, Musicmanager

mm = Musicmanager()
api = Mobileclient()
check = api.oauth_login(Mobileclient.FROM_MAC_ADDRESS)
if check == False:
    api.perform_oauth()
    api.oauth_login(Mobileclient.FROM_MAC_ADDRESS)
check = mm.login()
if check == False:
    mm.perform_oauth()
    mm.login()
plid = ""
def createplist(name):
    global plid
    plid = api.create_playlist(name)
    
def upload(path):
    mm.upload(path)
    addplaylist(path)

sids = []


def addplaylist(title):
    lst = mm.get_uploaded_songs()
    sid = ""
    for i in lst:
        if(i["title"]==title):
            sid = i["id"]
            break
    sids.append(sid)

def appendtoplaylist():
    global plid
    api.add_songs_to_playlist(plid, sids)