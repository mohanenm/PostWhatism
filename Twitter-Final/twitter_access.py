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

api = tweepy.API(auth)

'''
auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
'''
class tweets_galore(tweepy.Cursor):


    results = []
    # Get the first 1000 items based on the search query and store it
    for tweet in tweepy.Cursor(api.search, q='%23nietzsche').items(20):
        results.append(tweet.text)

    for tweet1 in tweepy.Cursor(api.search, q='%23freud').items(20):
        results.append(tweet1.text)

    for tweet2 in tweepy.Cursor(api.search, q='%23russel').items(20):
        results.append(tweet2.text)

    for tweet3 in tweepy.Cursor(api.search, q='%23westernphil').items(20):
        results.append(tweet3.text)




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
