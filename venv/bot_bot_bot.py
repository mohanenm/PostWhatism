import os 
import time
import re
import collections
import nltk
from nltk import word_tokenize
from markovbot import MarkovBot

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

dirname = os.path.dirname(os.path.abspath(__file__))
freudText = os.path.join(dirname, 'freudCompleteWorks.txt')
bot.read(freudText)
freudTweets =  bot.generate_text(25)
'''
fTwo = (re.sub('[-,_[@?#*"%;()}0-9]', " ", data))
fThree = (fTwo.replace("SCENE" "ACT", " "))
finalSText = fThree'''

shakeText = os.path.join(dirname, 'shakeComplete.txt')
bot2.read(shakeText)
shakeTweets = bot2.generate_text(25)

russellText = os.path.join(dirname, 'russelMath.txt')
bot3.read(russellText)
russellTweets = bot3.generate_text(25)

west_phil_text = os.path.join(dirname, 'westPhil.txt')
bot4.read(west_phil_text)
westp_text = bot4.generate_text(25)


print(freudTweets)
print(shakeTweets)
print(russellTweets)
print(westp_text)
'''
Keys/Tokens: 
'''
cons_key ='TRXh3CDSFBnPuZziANbqssl1l'
cons_secret ='sIfuEEp6T8qluDkU3S9PLcINoIIqcp0SUTrnwVfvdWhNRlIS6G'
access_token ='863265431691436032-PH9ASi1r3tfXJY90i4HuCVVpcLhUJ6D'
access_token_secret ='POslJ4RgWsgL7BzUV1WY7xZaI9YXGMmSIFPwA2vcZt1Uf'

'''
Login, tweet-period
'''
bot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
bot.twitter_tweeting_start(days=0, hours=5, minutes=0, keywords=None, prefix=None, suffix = "#Freud")
bot2.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
bot2.twitter_tweeting_start(days=0, hours=5, minutes=0, keywords=None, prefix=None, suffix = "#Shakespeare")
bot3.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
bot3.twitter_tweeting_start(days=0, hours=5, minutes=0, keywords=None, prefix=None, suffix = "#Russell")
bot4.twitter_login(cons_key, cons_secret, access_token, access_token_secret)
bot4.twitter_tweeting_start(days=0, hours=5, minutes=0, keywords=None, prefix=None, suffix = "#WesternPhilosophy")
time.sleep(6400)


print(west_phil_text)