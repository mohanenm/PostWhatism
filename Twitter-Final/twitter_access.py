import os
import time
import re
import collections
import nltk
from nltk import word_tokenize
# from markovbot import MarkovBot
import numpy as np
import re, datetime, pandas as pd
import twitter
import tweepy
from tweepy.parsers import JSONParser
from tweepy.streaming import StreamListener

try:
    import json
except ImportError:
    import simplejson as json

'''idea for "tweet miner from mike roman via: git_userid = elaiken3'''

'''
Keys/Tokens: DO NOT PUSH THESE!
'''

cons_key = 'TRXh3CDSFBnPuZziANbqssl1l'
cons_secret = 'sIfuEEp6T8qluDkU3S9PLcINoIIqcp0SUTrnwVfvdWhNRlIS6G'
access_token = '863265431691436032-PH9ASi1r3tfXJY90i4HuCVVpcLhUJ6D'
access_token_secret = 'POslJ4RgWsgL7BzUV1WY7xZaI9YXGMmSIFPwA2vcZt1Uf'

auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

'''
auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
'''


class tweets_galore(tweepy.Cursor):

    import ast
    results = []
    # Get the first 1000 items based on the search query and store it

for tweet in tweepy.Cursor(api.search, q='%23nietzsche', parser=tweepy.parsers.JSONParser()).items(20):
    [json.dumps(tweet) for tweet in tweet]
    print(tweet)


for tweet in tweepy.Cursor(api.search, tweet_mode="extended", id=None, q='%23nietzsche', ).items(20):
    print(tweet)
    json.loads(tweet)
    tweet = ast.literal_eval(tweet)
    results.append(tweet)

for tweet1 in tweepy.Cursor(api.search, tweet_mode="extended", id=None, q='%23freud').items(20):
    json.loads(tweet1)
    tweet1 = ast.literal_eval(tweet1)
    results.append(tweet1)

for tweet2 in tweepy.Cursor(api.search, tweet_mode="extended", id=None, q='%23russel').items(20):
    json.loads(tweet2)
    tweet3 = ast.literal_eval(tweet2)
    results.append(tweet2)

for tweet3 in tweepy.Cursor(api.search, tweet_mode="extended", id=None, q='%23westernphil').items(20):
    json.loads(tweet3)
    tweet3 = ast.literal_eval(tweet3)
    results.append(tweet3)

'''
    def on_status(self, status):
       status.text

    def on_error(self, status_code):
        if status_code == 420:
            return False

        # This handles Twitter authetification and the connection to Twitter Streaming API
        # This line filter Twitter Streams to capture data by the keywords

    stream_listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=["#nietzsche", "#freud", "#russel", "#westernphilosophy"])

'''
