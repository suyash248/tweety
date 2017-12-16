from tweepy import Stream
from service.twitter.listener.tweety_listener import TweetyStreamDataListener
from settings import twitter_config
#from elasticsearch import Elasticsearch
#es = Elasticsearch()

class Tweety(object):
    def __init__(self, listener=TweetyStreamDataListener()):
        self.listener = listener
        self.__auth__ = None
        self.streamer = self.__streamer__()

    def __authenticate__(self):
        from tweepy import OAuthHandler
        self.__auth__ = OAuthHandler(twitter_config['consumer_key'], twitter_config['consumer_secret'])
        self.__auth__.set_access_token(twitter_config['access_token'], twitter_config['access_token_secret'])
        return self.__auth__ is not None

    def __streamer__(self):
        is_authenticated = self.__authenticate__()
        if is_authenticated:
            return Stream(self.__auth__, self.listener)
        return None

    def filter(self, keywords=None, async=True):
        self.streamer.filter(track=keywords, async=True)
