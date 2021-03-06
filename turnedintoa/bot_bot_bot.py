import collections
import os
import re
import time
from collections import defaultdict
from heapq import nlargest
from string import punctuation

import nltk
from markovbot import MarkovBot
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

bot = MarkovBot()
bot2 = MarkovBot()
bot3 = MarkovBot()
bot4 = MarkovBot()
''' 
clean data for shakespeare

data = open('shakeComplete.txt', 'r').read()
fOne = ''.join(filter(lambda x: not x.isdigit(), data))
fTwo = (re.sub('[0-9\W]+', " ", fOne))
fThree = (fTwo.replace("SCENE", " "))
fFour = (fThree.replace("ACT", " "))
finalDataShake = fFour
'''
'''freud'''

''' 
i need to clean this up a lot and add organon
- make methods more recycle --> code is stale
- many authors at once with func 
- add learning method --> possible neural net? I want to make training worthwhile....
- add a score to output? compare results to text --> give score and only release the 'good' ones -> but also tell the model that it did a good or bad job
'''

dirname = os.path.dirname(os.path.abspath(__file__))
freudText = os.path.join(dirname, 'training_txt/freudCompleteWorks.txt')
bot.read(freudText)
freudTweets = bot.generate_text(25)
'''
fTwo = (re.sub('[-,_[@?#*"%;()}0-9]', " ", data))
fThree = (fTwo.replace("SCENE" "ACT", " "))
finalSText = fThree'''



''' really????? this is no good, going to fix this week '''
shakeText = os.path.join(dirname, 'training_txt/shakeComplete.txt')
bot2.read(shakeText)
shakeTweets = bot2.generate_text(25)

west_phil_text = os.path.join(dirname, 'training_txt/westPhil.txt')
bot4.read(west_phil_text)
westp_text = bot4.generate_text(25)

russellText = os.path.join(dirname, 'rtraining_txt/russelMath.txt')
bot3.read(russellText)
russellTweets = bot3.generate_text(25)

west_phil_text = os.path.join(dirname, 'training_txt/westPhil.txt')
bot4.read(west_phil_text)
westp_text = bot4.generate_text(25)

print(freudTweets)
print(shakeTweets)
print(russellTweets)
print(westp_text)

# to compare generated tweets to our model in main_twitter
nietzTweets_gen = nietzTweets
freudTweets_gen = freudTeets

# to compare text to main_twitter
nietz_text = nietz_text
freud_text = freudText

# similarity of the two text documents * --> generated tweet and actual writing and twiiter posts:
# we can choose what we want to do

import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


'''Clean the text of the two documents we want to see the similarity of  '''


def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')


def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]


'''
Keys/Tokens: 
'''

cons_key = 'TRXh3CDSFBnPuZziANbqssl1l'
cons_secret = 'sIfuEEp6T8qluDkU3S9PLcINoIIqcp0SUTrnwVfvdWhNRlIS6G'
access_token = '863265431691436032-PH9ASi1r3tfXJY90i4HuCVVpcLhUJ6D'
access_token_secret = 'POslJ4RgWsgL7BzUV1WY7xZaI9YXGMmSIFPwA2vcZt1Uf'

# Login, tweet-period

bot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
bot.twitter_tweeting_start(days=0, hours=5, minutes=0, keywords=None, prefix=None, suffix="#Freud")
bot2.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
bot2.twitter_tweeting_start(days=0, hours=5, minutes=0, keywords=None, prefix=None, suffix="#Shakespeare")
bot3.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
bot3.twitter_tweeting_start(days=0, hours=5, minutes=0, keywords=None, prefix=None, suffix="#Russell")
bot4.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
bot4.twitter_tweeting_start(days=0, hours=5, minutes=0, keywords=None, prefix=None, suffix="#WesternPhilosophy")
time.sleep(6400)
