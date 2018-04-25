import twitter_access

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

# number of tweets with the correct hash_tags!

print(twitter_access.tweets_galore.result_nietz)

# nietzsche
nietzsche_tweets = twitter_access.tweets_galore.result_nietz
# freud
freud_tweets = twitter_access.tweets_galore.result_freud
# russel
# russel_tweets = twitter_access.tweets_galore.result_russel

# westernphil
# western_tweets = twitter_access.tweets_galore.tweet3


'''
tweet_text1 = russel_tweets
clean_text1 = [preprocess_text(x, fix_unicode=True, lowercase=True, no_urls=True, no_emails=True,
                               no_phone_numbers=True, no_currency_symbols=True, no_punct=True, no_accents=True)
               for x in russel_tweets]
'''




''' PUT TWEETS INTO A DATAFRAME!'''

# from ast import literal_eval as leval
# nietzsche_tweetsF = leval(tweet)

nietz_dataframe = pd.DataFrame(nietzsche_tweets)
freud_dataframe = pd.DataFrame(freud_tweets)


# russel_dataframe = pd.DataFrame(russel_tweets)
# westPhil_dataframe = pd.DataFrame(western_tweets)


from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# TfidfVectorizer to find ngrams!
vect = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
# One giant string of all tweets! -- > nietz
summaries = "".join(map(str, nietz_dataframe))
ngrams_summaries = vect.build_analyzer()(summaries)
Counter(ngrams_summaries).most_common(20)

vect = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')

# One giant string of all tweets! --> freud
summaries = "".join(map(str, nietz_dataframe))
ngrams_summaries = vect.build_analyzer()(summaries)
Counter(ngrams_summaries).most_common(20)
vect = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')

# One giant string of all tweets! --> russel
# summaries = "".join(russel_dataframe['text'])
# ngrams_summaries = vect.build_analyzer()(summaries)
# Counter(ngrams_summaries).most_common(200)
# vect = TfidfVectorizer(ngram_range=(2, 5), stop_words='english')

# One giant string of all tweets! --> west phil
# summaries = "".join(westPhil_dataframe['text'])
# ngrams_summaries = vect.build_analyzer()(summaries)
# Counter(ngrams_summaries).most_common(200)

# from nltk.tokenize import word_tokenize
# tokens = word_tokenize()

# stemming of words -- > cleaning text finally


from textacy.preprocess import preprocess_text

# def clean_text():
tweet_nietzsche = nietzsche_tweets
clean_text = [preprocess_text(x, fix_unicode=True, lowercase=True, no_urls=True, no_emails=True,
                              no_phone_numbers=True, no_currency_symbols=True, no_punct=True, no_accents=True)
              for x in tweet_nietzsche]

tweet_freud = freud_tweets
clean_text0 = [preprocess_text(x, fix_unicode=True, lowercase=True, no_urls=True, no_emails=True,
                               no_phone_numbers=True, no_currency_symbols=True, no_punct=True, no_accents=True)
               for x in tweet_freud]

tfv = TfidfVectorizer(ngram_range=(1, 2), max_features=2000)
X = tfv.fit_transform(tweet_nietzsche).todense()
print(X.shape)

tfv = TfidfVectorizer(ngram_range=(1, 2), max_features=2000)
X = tfv.fit_transform(tweet_freud).todense()
print(X.shape)


# Just spent > 30 minutes trying to git pip install to trust scikit download!
