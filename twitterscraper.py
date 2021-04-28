import tweepy
import pandas as pd

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

# OAuth 1a authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API instance and set limit notification
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

CEO = ["AlbertBourla","ArvindKrishna","Benioff","billgifford","CarolBTome","ChuckRobbins","CraigMenear","Dan_Schulman","DavidSolomon","Dirkvandeput","elonmusk","emo_jamie_dimon","FedExInternati1","finkd","GeoffMartha","hansvestberg","JeffBezos","jimfarley98","JimFitterling","JulieSweet","KarenSLynch","Kevin_Johnson","larryculpjr","MarvinREllison","MiebachMichael","MikeSievert","PGelsinger","ramonlaguarta","satyanadella","stevemollenkopf","sundarpichai","sundarpichai","ThomasAFanning","tim_cook","WarrenBuffett"]
CNT = [] # An array to be filled with follower count
STCNT = [] # An array to be filled with status count

for s in CEO:
    user = api.get_user(s) # connects to user via username from tweepy package
    cnt = str(user.followers_count) # sets follower count temporarily to cnt
    stcnt = str(user.statuses_count) # sets status count temporarily to stcnt
    CNT.append(cnt)# appends to an array
    STCNT.append(stcnt)# appends to an array
data = [[CEO], [CNT], [STCNT]] # inserts each array to data
df = pd.DataFrame(data) # uses DataFrame method from pandas
df.to_csv(r'C:\xampp\htdocs\csc2405\blank.csv')# exports to CSV



    