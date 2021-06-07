# TweetMiner function from Mike Roman; changed to help work in our case==> hashtags
import datetime

# idea for, and implementation of "tweet miner from mike roman via: git_userid = elaiken3
''' Various things are changed to fit our model/objective'''

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
access_token = "ENTER YOUR ACCESS TOKEN"
access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "ENTER YOUR API KEY"
consumer_secret = "ENTER YOUR API SECRET"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])

''' 
        hash_tags = [
            "nietzsche", "freud", "russel", "westernphilosophy"
        ]

        data = []
        last_tweet_id = False
        page = 1

        while page <= max_pages:

            if last_tweet_id:
                statuses = self.api.GetStreamFilter(track) #count=self.result_limit, max_id=last_tweet_id - 1, include_rts=mine_retweets)
                statuses = [_.AsDict() for _ in statuses]
            else:
                statuses = self.api.GetStreamFilter(track) #count=self.result_limit, include_rts=mine_retweets)
                statuses = [_.AsDict() for _ in statuses]

            for item in statuses:
                # Using try except here.
                # When retweets = 0 we get an error (GetUserTimeline fails to create a key, 'retweet_count')
                try:
                    mined = {
                        'tweet_id': item['id'],
                        'handle': item['user']['screen_name'],
                        'retweet_count': item['retweet_count'],
                        'text': item['full_text'],
                        'mined_at': datetime.datetime.now(),
                        'created_at': item['created_at'],
                    }

                except:
                    mined = {
                        'tweet_id': item['id'],
                        'handle': item['user']['screen_name'],
                        'retweet_count': 0,
                        'text': item['full_text'],
                        'mined_at': datetime.datetime.now(),
                        'created_at': item['created_at'],
                    }

                last_tweet_id = item['id']
                data.append(mined)

            page += 1

        return data

'''
