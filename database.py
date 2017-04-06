import mysql.connector


#All functions that interact with the database go here


class Database:
    #Template for what insert statements look like, table name/columns aren't right
    def insertEvent(self, eventStatus, hostID, explicit, eventName):
        print("Inserting a new event")
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO EVENT (eventStatus, hostID, explicit, eventName) "
            "VALUES(%s, %s, %s, %s)")
        data = (eventStatus, hostID, explicit, eventName)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def insertHost(self, hostID, playlistID, spotifyToken, spotifyUsername):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO HOST (hostID, playlistID, spotifyToken, spotifyUsername) "
           "VALUES(%s, %s, %s, %s)")
        data = (hostID, playlistID, spotifyToken, spotifyUsername)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def insertUser(self, userID, currentEvent, inEvent, hostID):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO USER (userID, currentEvent, inEvent, hostID) "
           "VALUES(%s, %s, %s, %s)")
        data = (userID, currentEvent, inEvent, hostID)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def insertSong(self, songID, eventID, voteCount, songName, artist, explicit, vetoCount, vetoBoolean):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO NEXTSONGS (songID, eventID, voteCount, songName, artist, explicit, vetoCount, vetoBoolean) "
           "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)")
        data = (songID, eventID, voteCount, songName, artist, explicit, vetoCount, vetoBoolean)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def getPlaylist(self, hostID):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT playlistID FROM HOST WHERE hostID = %s") % (hostID)
        cursor.execute(query)
        playlistID = cursor.fetchone()
        cursor.close()
        cnx.commit()
        cnx.close()

        return playlistID[0]

    def getHostSpotifyToken(self, hostID):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT spotifyToken FROM HOST WHERE hostID = %s") % (hostID)
        cursor.execute(query)
        token = cursor.fetchone()
        cursor.close()
        cnx.commit()
        cnx.close()

        return token[0]

    def getSongArtist(self, songName):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT artist FROM NEXTSONGS WHERE songName = '%s'") % (songName)
        cursor.execute(query)
        artist = cursor.fetchone()
        cursor.close()
        cnx.commit()
        cnx.close()
        if artist is not None:
            return artist[0]

    def getSongID(self, songName):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT songID FROM NEXTSONGS WHERE songName = '%s'") % (songName)
        cursor.execute(query)
        songID = cursor.fetchone()
        cursor.close()
        cnx.commit()
        cnx.close()
        if songID is not None:
            return songID[0]

    def joinEvent(self, currentEvent, inEvent, host):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor()
        query = ("INSERT INTO user (currentEvent, inEvent, host) "
           "VALUES(%s, %s, %s)")
        data = (currentEvent, inEvent, host)
        cursor.execute(query, data)
        cursor.close()
        cnx.commit()
        cnx.close()

    def getEventID(self, eventName):
        cnx = mysql.connector.connect(user='publicuser', password ='ChorusIsNumber1', 
            host='174.138.64.25', database ='mydb')
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT eventID FROM EVENT WHERE eventName = '" +eventName + "'")
        print(query)
        cursor.execute(query)
        result = cursor.fetchone()[0];
        cursor.close()
        cnx.commit()
        cnx.close()
        return result