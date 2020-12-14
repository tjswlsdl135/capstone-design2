import tweepy
import wget

twitter_consumer_key = "pTHQmNMSbD6BJnZ1XtA8sJXY8"
twitter_consumer_secret = "ibKCgEs4b39gBExp34PLWAjz8WrMVf3T7T2k8zm9AEFhuYJPmM"  
twitter_access_token = "1315520301308936192-ZKRdcGofYW5zW8WGhEwBDvB1l8c6rr"
twitter_access_secret = "6mOe9uD5n8cqssWM0HLTDVGnn3QV3j23JBq9m0rt6JzY8"

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)

api = tweepy.API(auth)

count=1

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        global count
        print(status.text)
        if 'media' in status.entities:
            for image in  status.entities['media']:
                # print(image['media_url'])
                f='photo'+str(count)+'.jpg'
                wget.download(image['media_url'], out=f)


        # print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['출장'])
# myStream.sample(languages=['ko'])