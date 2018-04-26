import miner

'''fixed import issue!'''

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
from tweepy import Stream
from tweepy.streaming import StreamListener

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

api = twitter.Api(consumer_key=cons_key, consumer_secret=cons_secret, access_token_key=access_token,
                   access_token_secret=access_token_secret)

'''
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = twitter.API(auth)
'''

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    tweets_final = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=["#nietzsche", "#freud", "#russel", "#westernphilosophy"])

'''get tweets according to some hash tag, in our case
   get tweets on the basis of the authors, which were 
   analyzed and had tweets generated for in the markov
   model!
'''
''' tweet miner pretty much does this all for us == >
# X ==> rows: panda df
nietzsche_x = api.GetStreamFilter(hashtag="nietzsche", count=200, include_rts=False)
nietzsche_x = [_.AsDict() for _ in nietzsche_x]
for element in nietzsche_x:
    print(element['id'])
    print(element['full_text'])
    print('--')

#Y ==> rows: panda df
nietzsche_y = api.GetStreamFilter(hashtag="nietzsche", count=20, max_id=935706980643147777, include_rts=False)
nietzsche_y = [_.AsDict() for _ in nietzsche_y]
for element in nietzsche_y:
    print(element['id'])
    print(element['full_text'])
    print('--')
'''

''' should return "dict"  --> '''
#type(nietzsche_y[0])
''' should return item of the dict  --> '''
#print(nietzsche_y[0]['id'])

# Result limit == count parameter from our GetUserTimeline()

miner = miner.TweetMiner(api, result_limit=200)
nietzsche_tweets = miner.mine_hash_tags(track="nietzsche")
freud_tweets = miner.mine_hash_tags(track="freud")
russel_tweets = miner.mine_hash_tags(track="russel")
west_phil_tweets = miner.mine_hash_tags(track="westernphilosophy")


'''IF YOU WANT TO SEE THEM PRINTED: UNCOMMENT!
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
'''

''' PUT TWEETS INTO A DATAFRAME!'''
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

# TfidfVectorizer to find ngrams!
vect = TfidfVectorizer(ngram_range=(2,5), stop_words='english')
# One giant string of all tweets! -- > nietz
summaries = "".join(nietz_dataframe['text'])
ngrams_summaries = vect.build_analyzer()(summaries)
Counter(ngrams_summaries).most_common(200)
vect = TfidfVectorizer(ngram_range=(2,5), stop_words='english')

# One giant string of all tweets! --> freud
summaries = "".join(freud_dataframe['text'])
ngrams_summaries = vect.build_analyzer()(summaries)
Counter(ngrams_summaries).most_common(200)
vect = TfidfVectorizer(ngram_range=(2,5), stop_words='english')

# One giant string of all tweets! --> russel
summaries = "".join(russel_dataframe['text'])
ngrams_summaries = vect.build_analyzer()(summaries)
Counter(ngrams_summaries).most_common(200)
vect = TfidfVectorizer(ngram_range=(2,5), stop_words='english')

# One giant string of all tweets! --> west phil
summaries = "".join(westPhil_dataframe['text'])
ngrams_summaries = vect.build_analyzer()(summaries)
Counter(ngrams_summaries).most_common(200)

from nltk.tokenize import word_tokenize
tokens = word_tokenize()
# stemming of words -- > cleaning text finally
from textacy.preprocess import preprocess_text

# def clean_text():
tweet_text = summaries['text'].values
clean_NLTK_text = [preprocess_text(x, fix_unicode=True, lowercase=True, no_urls=True, no_emails=True, no_phone_numbers=True, no_currency_symbols=True,no_punct=True, no_accents=True)
              for x in tweet_text]

print(tweet_text)

tfv = TfidfVectorizer(ngram_range=(2,4), max_features=2000)
X = tfv.fit_transform(clean_NLTK_text).todense()
print(X.shape)

''' Just spent > 30 minutes trying to git pip install to trust scikit download!'''



'''
import ast

results = []
# Get the first 1000 items based on the search query and store it

for data in tweepy.Cursor(api.search, q='%23nietzsche').items(20):
    tweet = json.load(data)
    for status in tweet:
        tweet.append(status)
    print(tweet["text"])

for tweet in tweepy.Cursor(api.search, tweet_mode="extended", id=None, q='%23nietzsche', ).items(20):
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