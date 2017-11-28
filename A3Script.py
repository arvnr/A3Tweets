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
# OBJECTIVE TWO: GET RETWEETS
retweetlist = []
t = get_tweets("CitronResearch")
for tweet in t:
    retweetlist.append(tweet.retweet_count)

for tweet in t:
    if tweet.retweet_count == max(retweetlist):
    retweettext = tweet.text
print "Citron Retweets: \"" + retweettext + " \" with a retweet count of " +str(max(list))"
# OBJECTIVE THREE: SHOPIFY TWEETS THAT MENTION CITRON
def get_tweets(screen_name):

    alltweets = []
    try:
        tweets = api.user_timeline(screen_name, count=20)
        print "tweets"
        alltweets.extend(tweets)
        oldest = alltweets[-1].id - 1
        print oldest
        print len(tweets)
        while len(tweets) > 0:
            tweets = api.user_timeline(screen_name, count=20, max_id=oldest)
            alltweets.extend(tweets)
            oldest = alltweets[-1].id -1
            print "..%s Retrieved" %(len)alltweets))
    except:
        user_profile = "broken"
    return alltweets
# GETTING TWEETS FROM TOBI
t1 = get_tweets("Tobi")

with open ('Tobitweets.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","user","created_at","text"])
    for tweets in t1:
        if "troll, citron" in tweet.text;
            writer.writerow([tweet.user.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
# GETTING TWEETS FROM SHOPIFY
t2 = get_tweets("Shopify")

with open ('Shopifytweets.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","user","created_at","text"])
    for tweets in t2:
        if "citron, CitronResearch" in tweet.text;
            writer.writerow([tweet.user.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])

# OBJECTIVE FOUR: CITRON TWEETS THAT MENTION FTC
t3 = get_tweets("CitronResearch")

with open ('FTCtweets.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","user","created_at","text"])
    for tweets in t3:
        if "FTC" in tweet.text;
            writer.writerow([tweet.user.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
