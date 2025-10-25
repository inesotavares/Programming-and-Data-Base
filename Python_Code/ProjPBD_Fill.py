import mysql.connector
import pandas as pd

# Import CSV's
data1 = pd.read_csv('User.csv')   #USER FILE
df_USER = pd.DataFrame(data1)

data2 = pd.read_csv('Song.csv')   #SONG FILE
df_SONG = pd.DataFrame(data2)

data3 = pd.read_csv('Artist.csv')   #ARTIST FILE
df_ARTIST  = pd.DataFrame(data3)

data4 = pd.read_csv('Playlist.csv')   #PLAYLIST FILE
df_PLAYLIST = pd.DataFrame(data4)

data5 = pd.read_csv('Device.csv')   #DEVICE FILE
df_DEVICE = pd.DataFrame(data5)

data6 = pd.read_csv ('Subscribe.csv')   #SUBSCRIBE_TO FILE
df_SUBSCRIBE = pd.DataFrame(data6)

data7 = pd.read_csv('Likes.csv')   #LIKES_THE FILE
df_LIKES = pd.DataFrame(data7)

data8 = pd.read_csv ('Belongs.csv')   #BELONGS_TO FILE
df_BELONGS = pd.DataFrame(data8)

data9 = pd.read_csv ('Played.csv')   #PLAYED_ON FILE
df_PLAYED = pd.DataFrame(data9)

data10 = pd.read_csv('Connected.csv')   #CONNECTED_TO FILE
df_CONNECTED = pd.DataFrame(data10)


mydb = mysql.connector.connect(
  host="<Input host>",
  user="<Input user>",
  password="<Input password>",
  database="spotmusic"
)

mycursor = mydb.cursor()

#USER
sql = "INSERT INTO USER (UserID, Name, Email, RegistrationDate, PlanType) VALUES (%s, %s, %s, %s, %s)"

for i, row in df_USER.iterrows():
	mycursor.execute(sql, tuple(row))
	mydb.commit()

#SONG
sql = "INSERT INTO SONG (SongID, Title, Genre, Duration, UEPlays, UEDownloads) VALUES (%s, %s, %s, %s, %s, %s)"

for i, row in df_SONG.iterrows():
	mycursor.execute(sql, tuple(row))
	mydb.commit()

#ARTIST
sql = "INSERT INTO ARTIST (SongID, Artist) VALUES (%s, %s)"

for i, row in df_ARTIST.iterrows():
	mycursor.execute(sql, tuple(row))
	mydb.commit()

#PLAYLIST
sql = "INSERT INTO PLAYLIST (PlaylistID, Title, Description, PrivacySetting, CreatorID, CreationDate) VALUES (%s, %s, %s, %s, %s, %s)"

for i, row in df_PLAYLIST.iterrows():
	mycursor.execute(sql, tuple(row))
	mydb.commit()

#DEVICE
sql = "INSERT INTO DEVICE (DeviceID, Type, Model, SCTotal, SCFree) VALUES (%s, %s, %s, %s, %s)"

for i, row in df_DEVICE.iterrows():
	mycursor.execute(sql, tuple(row))
	mydb.commit()

#SUBS
sql = "INSERT INTO SUBSCRIBE (UserID, PlaylistID, SubsDate) VALUES (%s, %s, %s)"

for i, row in df_SUBSCRIBE.iterrows():
	mycursor.execute(sql, tuple(row))
	mydb.commit()

#LIKES
sql = "INSERT INTO LIKES (UserID, SongID, LikeDate) VALUES (%s, %s, %s)"

for i, row in df_LIKES.iterrows():
	mycursor.execute(sql, tuple(row))
	mydb.commit()

#BELONGS
sql = "INSERT INTO BELONGS (SongID,PlaylistID) VALUES (%s, %s)"

for i, row in df_BELONGS.iterrows():
	mycursor.execute(sql, tuple(row))
	mydb.commit()

#PLAYED
sql = "INSERT INTO PLAYED (PlaylistID, DeviceID, PlayDate) VALUES (%s, %s, %s)"

for i, row in df_PLAYED.iterrows():
	mycursor.execute(sql, tuple(row))
	mydb.commit()

#CONNECTED
sql = "INSERT INTO CONNECTED (UserID, DeviceID, ConnectDate) VALUES (%s, %s, %s)"

for i, row in df_CONNECTED.iterrows():
	mycursor.execute(sql, tuple(row))
	mydb.commit()

