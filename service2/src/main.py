from api import rabbitMQ
from api import s3
from api import shazam
from api import spotify
from db import postgres_update



# rabbitMQ.recieve()
song_info_list = rabbitMQ.receive()
print(song_info_list)
id = song_info_list[0][0]
print('id:',id)
file_name = song_info_list[0][1]
print('file name:', file_name)
path = f'/Users/sara/Desktop/amirkabir/spring02-03/cloud computing/project1/service2/src/{file_name}'
s3.download_file(file_name,path)
spotifyID = shazam.get_spotifyID(file_name)
print('spotifyID:',spotifyID)
dbObj = postgres_update.postgresDataHandle()
dbObj.update_songID(spotifyID,id)
dbObj.update_status(id)