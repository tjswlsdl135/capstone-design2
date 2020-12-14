import tweepy
import wget
from PIL import Image
from pytesseract import *
from kafka import KafkaProducer
from kafka.errors import KafkaError

import json

# twitter api auth
twitter_consumer_key = "pTHQmNMSbD6BJnZ1XtA8sJXY8"
twitter_consumer_secret = "ibKCgEs4b39gBExp34PLWAjz8WrMVf3T7T2k8zm9AEFhuYJPmM"  
twitter_access_token = "1315520301308936192-ZKRdcGofYW5zW8WGhEwBDvB1l8c6rr"
twitter_access_secret = "6mOe9uD5n8cqssWM0HLTDVGnn3QV3j23JBq9m0rt6JzY8"

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)

api = tweepy.API(auth)

count=1

# kafka producer 선언
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], max_request_size=5242880)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        global count
        # 트위터 text
        print(status.text)
        if 'media' in status.entities:
            for image in  status.entities['media']:
                # 트위터 이미지
                # print(image['media_url'])
                f='photo'+str(count)+'.jpg'
                wget.download(image['media_url'], out=f)
                # OCR 텍스트 추출
                img = Image.open(f)
                text = pytesseract.image_to_string(img, lang='kor+eng')
                print(f)
                print(text)
                count+=1


        # print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['출장'])
# myStream.sample(languages=['ko'])