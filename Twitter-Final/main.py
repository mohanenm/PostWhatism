import os
import time
import re
import collections
import nltk
from nltk import word_tokenize
from markovbot import MarkovBot
import numpy as np
import twitter, re, datetime, pandas as pd

'''idea for "tweet miner from mike roman via: git_userid = elaiken3'''


'''
Keys/Tokens: DO NOT PUSH THESE!
'''
cons_key ='TRXh3CDSFBnPuZziANbqssl1l'
cons_secret ='sIfuEEp6T8qluDkU3S9PLcINoIIqcp0SUTrnwVfvdWhNRlIS6G'
access_token ='863265431691436032-PH9ASi1r3tfXJY90i4HuCVVpcLhUJ6D'
access_token_secret ='POslJ4RgWsgL7BzUV1WY7xZaI9YXGMmSIFPwA2vcZt1Uf'

''' considering splliting the calls and actual function to put 
    them into Panda DF; it could get rather messy without it!
'''
api = twitter.Api(
    cons_key         =   twitter_keys['cons_key'],
    cons_secret      =   twitter_keys['cons_secret'],
    access_token     =   twitter_keys['access_token'],
    access_token_secret  =   twitter_keys['access_token_secret'],
    tweet_mode = 'extended'
)
type(api)


'''get tweets according to some hash tag, in our case
   get tweets on the basis of the authors, which were 
   analyzed and had tweets generated for in the markov
   model!
'''

''' X ==> rows: panda df'''
nietzsche_x = api.GetHashTag(hash_tag="nietzsche", count=200, include_rts=False)
nietzsche_x = [_.AsDict() for _ in nietzsche_x]
for element in nietzsche_x:
    print(element['id'])
    print(element['full_text'])
    print('--')

''' Y ==> rows: panda df'''
nietzsche_y = api.GetUserTimeline(hash_tag="nietzsche", count=20, max_id=935706980643147777, include_rts=False)
nietzsche_y = [_.AsDict() for _ in nietzsche_y]
for element in nietzsche_y:
    print(element['id'])
    print(element['full_text'])
    print('--')






class GetTweets(object):


    def__init__(self, api, tweet_limit = 200):


    self.api = api
    self.result_limit = tweet_limit



