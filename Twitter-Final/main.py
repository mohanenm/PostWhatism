import os
import time
import re
import collections
import nltk
from nltk import word_tokenize
from markovbot import MarkovBot
import numpy as np
import twitter, re, datetime, pandas as pd
from miner.py import TweetMiner
frin

'''idea for "tweet miner from mike roman via: git_userid = elaiken3'''

'''
Keys/Tokens: DO NOT PUSH THESE!
'''
cons_key = 'TRXh3CDSFBnPuZziANbqssl1l'
cons_secret = 'sIfuEEp6T8qluDkU3S9PLcINoIIqcp0SUTrnwVfvdWhNRlIS6G'
access_token = '863265431691436032-PH9ASi1r3tfXJY90i4HuCVVpcLhUJ6D'
access_token_secret = 'POslJ4RgWsgL7BzUV1WY7xZaI9YXGMmSIFPwA2vcZt1Uf'

''' considering splliting the calls and actual function to put 
    them into Panda DF; it could get rather messy without it!
'''
api = twitter.Api(
    cons_key=twitter_keys['cons_key'],
    cons_secret=twitter_keys['cons_secret'],
    access_token=twitter_keys['access_token'],
    access_token_secret=twitter_keys['access_token_secret'],
    tweet_mode='extended'
)
type(api)

'''get tweets according to some hash tag, in our case
   get tweets on the basis of the authors, which were 
   analyzed and had tweets generated for in the markov
   model!
'''

''' X ==> rows: panda df'''
nietzsche_x = api.GetHashTag(hashtag="nietzsche", count=200, include_rts=False)
nietzsche_x = [_.AsDict() for _ in nietzsche_x]
for element in nietzsche_x:
    print(element['id'])
    print(element['full_text'])
    print('--')

''' Y ==> rows: panda df'''
nietzsche_y = api.GetUserTimeline(hashtag="nietzsche", count=20, max_id=935706980643147777, include_rts=False)
nietzsche_y = [_.AsDict() for _ in nietzsche_y]
for element in nietzsche_y:
    print(element['id'])
    print(element['full_text'])
    print('--')

''' should return "dict"  --> '''
type(nietzsche_y[0])
''' should return item of the dict  --> '''
nietzsche_y[0]['id']

# Result limit == count parameter from our GetUserTimeline()

miner = TweetMiner(api, result_limit=200)
nietzsche_tweets = miner.mine_user_tweets(hashtag="nietzsche")
freud_tweets = miner.mine_user_tweets(hashtag="freud")
russel_tweets = miner.mine_user_tweets(hashtag="russel")
west_phil_tweets = miner.mine_user_tweets(hashtag="westernphilosophy")

for x in range(5):
    print(nietzsche_tweets[x]['text'])
    print('---')
for x in range(5):
    print(freud_tweets[x]['text'])
    print('---')
for x in range(5):
    print(russel_tweets[x]['text'])
    print('---')
for x in range(5):
    print(west_phil_tweets[x]['text'])
    print('---')

nietz_dataframe = pd.DataFrame(nietzsche_tweets)
freud_dataframe = pd.DataFrame(freud_tweets)
russel_dataframe = pd.DataFrame(russel_tweets)
westPhil_dataframe = pd.DataFrame(west_phil_tweets)


from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# We can use the TfidfVectorizer to find ngrams for us
vect = TfidfVectorizer(ngram_range=(2,5), stop_words='english')

# Pulls all of trumps tweet text's into one giant string
summaries = "".join(nietz_dataframe['text'])
ngrams_summaries = vect.build_analyzer()(summaries)

Counter(ngrams_summaries).most_common(20)

''' Just spent > 30 minutes trying to git pip install to trust scikit download!'''
