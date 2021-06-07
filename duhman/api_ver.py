import collections
import datetime
import os
import re
import re
import time

import nltk
# from markovbot import MarkovBot
import numpy as np
import pandas as pd
import tweepy
import twitter
from TwitterSearch import *
from nltk import word_tokenize
from tweepy.parsers import JSONParser
from tweepy.streaming import StreamListener


'''
Keys/Tokens: DO NOT PUSH THESE!
'''

cons_key = ''
cons_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

'''
auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
'''


class tweets_galore(TwitterSearch):
    try:
        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
        tso.set_keywords(['#nietzsche', '-filter:retweets',
                          '-filter:replies'])  # let's define all words we would like to have a look for
        tso.set_language('en')  # we want to see english only
        tso.set_include_entities(False)  # and don't give us all those entity information
        tso.tweet_mode = 'extended'
        tso.set_count(100)
        tso.set_link_filter()  # filter hyper links
        result_nietz = []

        ts = TwitterSearch(cons_key, cons_secret, access_token, access_token_secret)

        for tweet in ts.search_tweets_iterable(tso):
            tweets = (tweet['text'], 'nietzsche')
            result_nietz.append(tweets)

    except TwitterSearchException as e:  # take care of all those ugly errors if there are some
        print(e)

    try:
        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
        tso.set_keywords(['#freud', '-filter:retweets',
                          '-filter:replies'])  # let's define all words we would like to have a look for
        tso.add_keyword(["", '"'], or_operator=False)
        tso.set_language('en')  # we want to see english only
        tso.set_include_entities(False)  # and don't give us all those entity information
        tso.tweet_mode = 'extended'
        tso.set_count(100)
        tso.set_link_filter()  # filter hyper links
        result_freud = []

        ts = TwitterSearch(cons_key, cons_secret, access_token, access_token_secret)

        for tweet in ts.search_tweets_iterable(tso):
            tweets = (tweet['text'], 'freud')
            result_freud.append(tweets)

    except TwitterSearchException as e:  # take care of all those ugly errors if there are some
        print(e)


"""
        try:
            tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
            tso.set_keywords(['#russel', '-filter:retweets',
                              '-filter:replies'])  # let's define all words we would like to have a look for
            tso.set_language('en')  # we want to see english only
            tso.set_include_entities(False)  # and don't give us all those entity information
            tso.set_count(0)
            tso.set_link_filter()  # filter hyper links
            result_russel = []

            ts = TwitterSearch(cons_key, cons_secret, access_token, access_token_secret)

            for tweet in ts.search_tweets_iterable(tso):
                tweets = '@%s tweeted: %s' % (['user'], tweet['text'])
                result_russel.append(tweets)

        except TwitterSearchException as e:  # take care of all those ugly errors if there are some
            print(e)
"""


## for tests!

''' 
try:
    tuo = TwitterUserOrder('NietzscheQuotes')
    tuo.set_count(0)
    tuo.set_exclude_replies(True)
    tuo.set_include_rts(False)

    f_test = []

    ts = TwitterSearch(cons_key, cons_secret, access_token, access_token_secret)
    for tweet in ts.search_tweets_iterable(tuo):
        print((tweet['text']))
        f_test.append(tweet)

except TwitterSearchException as e:  # take care of all those ugly errors if there are some
    print(e)
'''
