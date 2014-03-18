import pafy
import gdata.youtube
import gdata.youtube.service
import os.path

yt_service = gdata.youtube.service.YouTubeService()
yt_service.ssl = True

def getVideoUrl(search_term):
    yt_service = gdata.youtube.service.YouTubeService()
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.vq = search_term
    query.max_results = 1
    feed = yt_service.YouTubeQuery(query)
    for i in feed.entry:
        vurl = i.media.player.url
        break
    return vurl

songfile = open('nc_playlist.txt')
songs = songfile.readlines()
songfile.close()

for song in songs:
    song = song.replace('\r','')
    song = song.replace('\n','')
    if os.path.isfile('songs/' + song + '.m4a'):
        continue
    url = getVideoUrl(song)
    url = url.split('&')[0]
    video = pafy.new(url)
    audio = video.getbestaudio()
    if audio == None:
        print "Couldn't get m4a of " + song
        continue
    if audio.extension == 'm4a':
        audio.download(quiet=False,filepath= 'songs/' + song + '.' + audio.extension)
    else:
        a=0
        print 'what'
        streams = video.audiostreams
        for stream in streams:
            if stream.extension == 'm4a':
                stream.download(quiet=False,filepath= 'songs/' + song + '.' + stream.extension)
                a=1
                break
        if a==0:
            print "Couldn't get m4a of " + song
