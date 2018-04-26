import os, sys
import api_ver  # import api calls/search
# from venv import bot_bot_bot  # import parent

'''fixed import issue!'''

import time
import re
import collections
import nltk
from nltk import word_tokenize
# from markovbot import MarkovBot
import numpy as np
import re, datetime, pandas as pd

# number of tweets with the correct hash_tags!

print(api_ver.tweets_galore.result_nietz)

'''
tweet_text1 = russel_tweets
clean_text1 = [preprocess_text(x, fix_unicode=True, lowercase=True, no_urls=True, no_emails=True,
                               no_phone_numbers=True, no_currency_symbols=True, no_punct=True, no_accents=True)
               for x in russel_tweets]
'''

''' PUT TWEETS INTO A DATAFRAME!'''

# nietzsche
nietzsche_tweets = api_ver.tweets_galore.result_nietz
# freud
freud_tweets = api_ver.tweets_galore.result_freud
# russel
# russel_tweets = api_ver.tweets_galore.result_russel

# westernphil
# western_tweets = api_ver.tweets_galore.tweet3

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

tfv = TfidfVectorizer(ngram_range=(2, 5), max_features=2000) # changed range
X = tfv.fit_transform(clean_text).todense()
print(X.shape)

# types of search, regression, etc

from sklearn.model_selection import GridSearchCV

lr = LogisticRegression()
params = {'penalty': ['l1', 'l2'], 'C': np.logspace(-5, 0, 100)}
# Grid searching to find optimal parameters for Logistic Regression
gs = GridSearchCV(lr, param_grid=params, cv=2, verbose=1)
gs.fit(X, y)

print(gs.best_params_)
print(gs.best_score_)
# Just spent > 30 minutes trying to git pip install to trust scikit download!

from sklearn.model_selection import cross_val_score

accuracies = cross_val_score(LogisticRegression(), X, y, cv=2)

print(accuracies.mean())
print(1 - y.mean())

# check our model based on generated tweets....

estimator = LogisticRegression(penalty='l2', C=1.0)
estimator.fit(X, y)


# wait unitl count fixed
# n_test = api_ver.tweets_galore.f_test
n_test = [
 "To live is to suffer, to survive is to find some meaning in the suffering. #Nietzsche"
]

# wait unitl count fixed
# f_test = api_ver.tweets_galore.f_test

Xtest = tfv.transform(n_test)
pd.DataFrame(estimator.predict_proba(Xtest), columns=["Proba_nietzsche", "Proba_freud"])

Xtest = tfv.transform(n_test)
pd.DataFrame(estimator.predict_proba(Xtest), columns=["Proba_nietzsche", "Proba_freud"])



# tweet extraction


# extracting tweets with highest niet, freud proba ==>

estimator.predict_proba(X)
Probas_x = pd.DataFrame(estimator.predict_proba(X), columns=["Proba_nietzsche", "Proba_freud"])
joined_x = pd.merge(tweets, Probas_x, left_index=True, right_index=True)
print(joined_x)


# actually printing those tweets out

# nietzsche

# --> max
joined_n = joined_x[joined_x['handle'] == "nietzsche"]
for el in joined_n[joined_n['Proba_nietzsche'] == max(joined_n['Proba_nietzsche'])]['text']:
    print(el)
# --> min
for el in joined_n[joined_n['Proba_nietzsche'] == min(joined_n['Proba_nietzsche'])]['text']:
    print(el)

# freud

# --> max
joined_f = joined_x[joined_x['handle'] == "freud"]
for el in joined_f[joined_n['Proba_freud'] == max(joined_f['Proba_freud'])]['text']:
    print("MAX")
    print(el)
# --> min
for el in joined_f[joined_f['Proba_freud'] == min(joined_f['Proba_freud'])]['text']:
    print("MIN")
    print(el)
