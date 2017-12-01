#Taken from ECMM600 Lab 4 - Modify Tweets with Python and Twitter API by Colin Conrad
#Twitter Profiler app. This is a simple script to configure the Twitter API

import tweepy, time, csv

# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview
consumer_key = "ps6WGQd2QMDOz0R1sAklRf5tP"
consumer_secret = "91qmrLhdc1qbDk0UnSSDSInOg48NffaLcCp1YGUXKBwSvHHPem"
access_key = "24336411-jVLnipLfqMBzzV2US1UbP9SmpY5l9MlFHeqWbucjh"
access_secret = "wA1sSoy91kfanMrpfoRE8eSRqSsXYYUR2dsjuWVzXcAjw"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    try:
        #https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"
    return user_profile

# OBJECTIVE ONE: GET TWITTER USER ID
s = get_profile("CitronResearch")
print "Name:" +s.name
print "id:" +s.id_str

def get_tweets(screen_name):
    try:
        tweets = api.user_timeline(screen_name = screen_name,count = 20)
    except:
        tweets = "broken"
    return tweets

# uses the function to query a Twitter user. Try s = get_profile("cd_conrad")
profiles = ["Shopify", "CitronResearch"]

with open ('arvinrA3.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","user","created_at","text"])
    for profile in profiles:
        t = get_tweets(profile)
        for tweet in t:
            writer.writerow([tweet.user.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
