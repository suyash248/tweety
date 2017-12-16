from tweepy.streaming import StreamListener
import json

class TweetyStreamDataListener(StreamListener):
    # on success
    def on_status(self, status):
        data = status._json

        #print dict_data
        print "@{author} : {tweet}".format(author=data["user"]["screen_name"].encode('utf-8'),
                                           tweet=data["text"].encode('utf-8'))

        # es.index(index="tweetstream",
        #          doc_type="tweet",
        #          body={"author": dict_data["user"]["screen_name"],
        #                "date": dict_data["created_at"],
        #                "message": dict_data["text"]})
        return True

    # on failure
    def on_error(self, status):
        print status