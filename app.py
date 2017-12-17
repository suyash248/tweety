import json
from flask import Flask, request

app = Flask(__name__)

from views.funnel import funnel
app.register_blueprint (funnel, url_prefix='/funnel')

@app.route('/')
def index():
    from tweety import Tweety
    Tweety().filter(keywords=['cricket'])
    return 'Welcome to Tweety!'

@app.route('/test')
def test():
    from service.esutil.querybuilder.query_builder import QueryBuilder
    criteria = {
        "AND": [
            {
                "fields": ['tweet_text'],
                "operator": "contains",
                "query": "league"
            }, {
            #             Twitter for Android
                "fields": ['source_device'],
                "operator": "equals",
                "query": "Twitter for Android"
            }
        ],
        # "NOT": [
        #     {
        #         "fields": ['source_device'],
        #         "operator": "contains",
        #         "query": "Android"
        #     }
        # ],
        "OR": [
            {
                "fields": ['screen_name'],
                "operator": "startswith",
                "query": "rahul*"
            }
        ]
    }

    s = QueryBuilder(criteria).search()
    print QueryBuilder.get_raw_query(s)
    for hit in s:
        print hit.tweet_text
        print hit.screen_name
        print hit.source_device
        print "\n-----------------------------------------------------------------\n"
    # from service.esutil import dsl_search
    # from elasticsearch_dsl import Q
    # q = Q("multi_match", query='cricket', fields=['tweet_text'])
    # s = dsl_search.query(q)
    # print s.to_dict()
    #
    # print s.execute()
    # for hit in s:
    #     print hit.tweet_text
    #
    return "Testing"


if __name__ == '__main__':
    app.run()
