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
print "Name: " + s.name
print "id: " + s.id_str
def get_tweets(screen_name):
    alltweets = []
    try:
        #https://developer.twitter.com/en/docs/tweets/timelines/overview describes user_timeline
        tweets = api.user_timeline(screen_name, count=3200)
        print "tweets"
        alltweets.extend(tweets)
        oldest = alltweets[-1].id - 1
        print oldest
        print len(tweets)
        while len(tweets) > 0:
            tweets = api.user_timeline(screen_name, count=3200, max_id=oldest)
            alltweets.extend(tweets)
            oldest = alltweets[-1].id - 1
            print "...Fetching Tweets" % (len(alltweets))
    except:
        user_profile = "broken"
    return alltweets
       
list1 = []
t = get_tweets("CitronResearch")
for tweet in t:
    list1.append(tweet.retweet_count)

for tweet in t:
    if tweet.retweet_count == max(list1):
        text1 = tweet.text

with open ('A3Export.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","user","created_at","text"])
    for tweet in t:
        if "FTC" in tweet.text:
            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
    t3 = get_tweets("Shopify")
    for tweet in t3:
        if "citron" in tweet.text:
            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text.encode('unicode-escape')])
print "Most Retweeted Tweet by Citron: \"" + text1 + " \" count of " +str(max(list1))
