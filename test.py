from gmusicapi import Mobileclient, Musicmanager

mm = Musicmanager()
mm.perform_oauth()
mm.login()
mm.upload("test.mp3")