import mysql.connector

mydb = mysql.connector.connect(
  host="<Input host>",
  user="<Input user>",
  password="<Input password>",
  database="spotmusic"
)

mycursor = mydb.cursor()

print("How many users does the database has?")
mycursor.execute("SELECT COUNT(UserId) FROM USER")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
input("Press <Enter> to continue...")

print("What devices do users use?")
mycursor.execute("SELECT DISTINCT Type FROM DEVICE")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
input("Press <Enter> to continue...")

print("What is the name and the plan type of the first subscriber?")
mycursor.execute("SELECT Name, PlanType FROM USER ORDER BY RegistrationDate DESC LIMIT 1")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
input("Press <Enter> to continue...")

print("What playlist is the most popular?")
mycursor.execute("SELECT PLAYLIST.Title, COUNT(PLAYED.PlaylistID) as Num FROM PLAYED JOIN PLAYLIST ON PLAYED.PlaylistID=PLAYLIST.PlaylistID GROUP BY PLAYED.PlaylistID ORDER BY Num DESC")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
input("Press <Enter> to continue...")

print("How many average downloads songs have?")
mycursor.execute("SELECT AVG(UEDownloads) FROM SONG")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
input("Press <Enter> to continue...")

print("What genre has more appearences")
mycursor.execute("SELECT Genre, COUNT(SongID) as Num FROM SONG GROUP BY Genre ORDER BY NUM Desc")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
input("Press <Enter> to continue...")

print("What is the Title and Creation Date of the playlists that Taylor Swift features since 2020, inclusively?")
mycursor.execute("SELECT DISTINCT(PLAYLIST.Title), PLAYLIST.CreationDate FROM (PLAYLIST JOIN BELONGS ON PLAYLIST.PlaylistID = BELONGS.PlaylistID JOIN SONG ON SONG.SongID= BELONGS.SongID JOIN ARTIST ON ARTIST.SongID=SONG.SongID) WHERE Artist='Taylor Swift' AND YEAR(CreationDate)>2019 ORDER BY PLAYLIST.Title")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
input("Press <Enter> to continue...")

print("End of Queries")
