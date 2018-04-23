# idea for, and implementation of "tweet miner from mike roman via: git_userid = elaiken3
# TweetMiner function from Mike Roman



''' Various things are changed to fit our model/objective'''
class TweetMiner(object):

    def __init__(self, api, result_limit=20):

        self.api = api
        self.result_limit = result_limit

    def mine_user_tweets(self, user="HillaryClinton", mine_retweets=False, max_pages=20):

        data = []
        last_tweet_id = False
        page = 1

        while page <= max_pages:

            if last_tweet_id:
                statuses = self.api.GetUserTimeline(hashtag=user, count=self.result_limit, max_id=last_tweet_id - 1,
                                                    include_rts=mine_retweets)
                statuses = [_.AsDict() for _ in statuses]
            else:
                statuses = self.api.GetUserTimeline(screen_name=user, count=self.result_limit,
                                                    include_rts=mine_retweets)
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