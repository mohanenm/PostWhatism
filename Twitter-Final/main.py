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


class GetTweets(object):


    def__init__(self, api, tweet_limit = 200):


    self,api = api
    self.result_limit = tweet_limit



