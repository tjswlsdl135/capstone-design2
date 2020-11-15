import twitter
import tweepy
import requests

twitter_consumer_key = "pTHQmNMSbD6BJnZ1XtA8sJXY8"
twitter_consumer_secret = "ibKCgEs4b39gBExp34PLWAjz8WrMVf3T7T2k8zm9AEFhuYJPmM"  
twitter_access_token = "1315520301308936192-ZKRdcGofYW5zW8WGhEwBDvB1l8c6rr"
twitter_access_secret = "6mOe9uD5n8cqssWM0HLTDVGnn3QV3j23JBq9m0rt6JzY8"

# twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
#                           consumer_secret=twitter_consumer_secret, 
#                           access_token_key=twitter_access_token, 
#                           access_token_secret=twitter_access_secret)

# account = "@tjswlsdl135"
# statuses = twitter_api.GetUserTimeline(screen_name=account, count=200, include_rts=True, exclude_replies=False)
# #print(statuses)

# for status in statuses:
#     print("하하")
#     print(status)
#     print("하하하")
#     print(status.text)
#     #     print(status.text.encode('utf-8'))

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)

auth.set_access_token(twitter_access_token, twitter_access_secret)

api = tweepy.API(auth)

timeline = api.user_timeline(count = 10)

for tweet in timeline:
    print("text")
    print(tweet.text)
    for media in tweet.entities.get("media", [{}]):
        print("media")
        print(media)
        if media.get("type", None) == "photo":
            image_content = requests.get(media["media_url"])
            print("image")
            print(image_content.content)
            
# result = []
# for i in range(0,2):
#     tweets = api.search(keyword)
#     for tweet in tweets:
#         result.append(tweet)
#         print("하하하")
#         print(tweet)

#print(result)