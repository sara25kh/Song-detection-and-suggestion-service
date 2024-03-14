from api import spotify
from api import mailgun
from db import postgres_getInfo

dbObj = postgres_getInfo.postgresDataHandle()
trackID = dbObj.get_songID()
# trackID = '2tZ9SSCDM5uJS8ZXGdfvCf'
recommendations = spotify.get_recommendations(trackID)
print('recommendations:',recommendations)
mailgun.send_simple_message(recommendations)