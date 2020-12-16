import tweepy
import wget
import os
from PIL import Image
from pytesseract import *
from kafka import KafkaProducer
from kafka.errors import KafkaError
from collections import OrderedDict

import json

# twitter api auth
twitter_consumer_key = "pTHQmNMSbD6BJnZ1XtA8sJXY8"
twitter_consumer_secret = "ibKCgEs4b39gBExp34PLWAjz8WrMVf3T7T2k8zm9AEFhuYJPmM"  
twitter_access_token = "1315520301308936192-ZKRdcGofYW5zW8WGhEwBDvB1l8c6rr"
twitter_access_secret = "6mOe9uD5n8cqssWM0HLTDVGnn3QV3j23JBq9m0rt6JzY8"

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)

api = tweepy.API(auth)

# count=1

# kafka producer 선언
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], max_request_size=5242880)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # global count
        # 트위터 text
        text = status.text
        # json 생성
        file_data = OrderedDict()
        file_data["text"] = str(text.encode('utf-8'))
        file_data["OCRtext"]=""
        if 'media' in status.entities:
            for image in  status.entities['media']:
                # 트위터 이미지
                # print(image['media_url'])
                # f='photo'+str(count)+'.jpg'
                f = 'photo.jpg'
                wget.download(image['media_url'], out=f)

                # OCR 텍스트 추출
                img = Image.open(f)
                OCRtext = pytesseract.image_to_string(img, lang='kor+eng')
                print(text)
                print(OCRtext)
                print(str(text.encode('utf-8')))
                file_data["OCRtext"]=OCRtext.encode('utf-8')
                file_name = './' + f
                if os.path.isfile(file_name):
                    os.remove(file_name)
                # count+=1
            
        # produce
        future = producer.send('testTopic', json.dumps(file_data).encode('utf-8'))
        try:
            recorde_metadata = future.get(timeout=10)
        except KafkaError:
            pass
        # print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)


myStream.filter(track=['출장'])
# myStream.sample(languages=['ko'])