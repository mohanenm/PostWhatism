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



'''
tweet_text1 = russel_tweets
clean_text1 = [preprocess_text(x, fix_unicode=True, lowercase=True, no_urls=True, no_emails=True,
                               no_phone_numbers=True, no_currency_symbols=True, no_punct=True, no_accents=True)
               for x in russel_tweets]
'''




''' PUT TWEETS INTO A DATAFRAME!'''

# nietzsche
nietzsche_tweets = twitter_access.tweets_galore.result_nietz
# freud
freud_tweets = twitter_access.tweets_galore.result_freud
# russel
# russel_tweets = twitter_access.tweets_galore.result_russel

# westernphil
# western_tweets = twitter_access.tweets_galore.tweet3

# from ast import literal_eval as leval
# nietzsche_tweetsF = leval(tweet)

nietz_df = pd.DataFrame(nietzsche_tweets)
nietz_df.columns = ['text', 'handle']
freud_df = pd.DataFrame(freud_tweets)
freud_df.columns = ['text', 'handle']

tweets = pd.concat([nietz_df, freud_df], axis=0)

print(tweets)

# russel_dataframe = pd.DataFrame(russel_tweets)
# westPhil_dataframe = pd.DataFrame(western_tweets)


from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# TfidfVectorizer to find ngrams!
vect = TfidfVectorizer(ngram_range=(2, 5), stop_words='english')
# One giant string of all tweets! -- > nietz
summaries = "".join(nietz_df['text'])
ngrams_summaries = vect.build_analyzer()(summaries)
Counter(ngrams_summaries).most_common(20)

vect = TfidfVectorizer(ngram_range=(2, 5), stop_words='english')
# One giant string of all tweets! --> freud
summaries = "".join(freud_df['text'])
ngrams_summaries = vect.build_analyzer()(summaries)
Counter(ngrams_summaries).most_common(20)


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
tweet_nietzsche = tweets['text'].values
clean_text = [preprocess_text(x, fix_unicode=True, lowercase=True, no_urls=True, no_emails=True,
                              no_phone_numbers=True, no_currency_symbols=True, no_punct=True, no_accents=True)
              for x in tweet_nietzsche]


print(tweet_nietzsche)

y = tweets['handle'].map(lambda x: 1 if x == 'nietzsche' else 0).values
print(max(pd.Series(y).value_counts(normalize=True)))

y = tweets['handle'].map(lambda x: 1 if x == 'freud' else 0).values
print(max(pd.Series(y).value_counts(normalize=True)))


tfv = TfidfVectorizer(ngram_range=(1, 2), max_features=2000)
X = tfv.fit_transform(clean_text).todense()
print(X.shape)

from sklearn.model_selection import GridSearchCV

lr = LogisticRegression()
params = {'penalty': ['l1', 'l2'], 'C':np.logspace(-5,0,100)}
#Grid searching to find optimal parameters for Logistic Regression
gs = GridSearchCV(lr, param_grid=params, cv=2, verbose=1)
gs.fit(X, y)

print(gs.best_params_)
print(gs.best_score_)


# Just spent > 30 minutes trying to git pip install to trust scikit download!
