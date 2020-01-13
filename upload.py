from gmusicapi import Mobileclient, Musicmanager

mm = Musicmanager()
api = Mobileclient()
# api.perform_oauth()
api.oauth_login(Mobileclient.FROM_MAC_ADDRESS)
# mm.perform_oauth()
mm.login()
plid = ""
def createplist(name):
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
    print("F")
    print(sids)
    api.add_songs_to_playlist(plid, sids)