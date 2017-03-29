import spotipy
import spotipy.util as util

#All functions that interact directly with the Spotify API go here

class Spotify:
    def getUserName(self):
        return '1210281728'

    def getToken(self):
        username =  '1210281728'
        playlist_name = 'Chorus'
        scope = 'playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify'
        #put server url for redirect url
        token = util.prompt_for_user_token(username,scope,client_id='3c6df9a90b934200856b352829f09fd0',client_secret='694b8ac2f8cb478796b304fd6f1fd082',redirect_uri='http://localhost/')
        return token

    def createPlaylist():
        #refresh_access_token(
        # Creates a playlist for a user
        username = '1210281728'
        #username =  '1235536440'
        playlist_name = 'Chorus3'
        scope = 'playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify'

        #put server url for redirect url
        token = util.prompt_for_user_token(username,scope,client_id='3c6df9a90b934200856b352829f09fd0',client_secret='694b8ac2f8cb478796b304fd6f1fd082',redirect_uri='http://localhost/')

        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            playlists = sp.user_playlist_create(username, playlist_name)
            pprint.pprint(playlists)
            return token
        else:
            print("Can't get token for", username)
            return 0;

    def addSongs(token):
        username = '1210281728'
        #username = '1235536440'

        track_ids = ["2gFvRmQiWg9fN9i74Q0aiw", "4Km5HrUvYTaSUfiSGPJeQR", "7BKLCZ1jbUBVqRi2FVlTVw", "3bi8yEuK44vLcbjHkPH0u1", "5SDVX9gpSXoE0M6KZt4EBF", "0O6jl8Zamz6TGF0nUwMQsF", "4RnfMhMUMqHlrn4V6A3KfS", "6F5c58TMEs1byxUstkzVeM", "3cfOd4CMv2snFaKAnMdnvK"]
        #scope = 'playlist-read-private playlist-read-collaborative playlist-modify-private'
        #token = util.prompt_for_user_token(username,scope,client_id='3c6df9a90b934200856b352829f09fd0',client_secret='694b8ac2f8cb478796b304fd6f1fd082',redirect_uri='http://localhost/')
        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        # find album by name
        playlists = sp.user_playlists(username, limit=50, offset=0)

        # get the first album uri
        for playlist in playlists['items']:
            if(playlist['name'] == "Chorus3"):
                playlist_id = playlist['id']

        #playlist_id = '59E9xmQUzDY7H9yKNlj48F'
        print track_ids
        sp.user_playlist_add_tracks(username, playlist_id, track_ids)
        print("playlist id: " + playlist_id)
        return playlist_id