from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    from tweety import Tweety
    Tweety().filter(keywords=['cricket'])
    return 'Welcome to Tweety!'

@app.route('/', methods=["POST"])
def search():
    pass

@app.route('/test')
def test():
    from service.esutil.querybuilder.query_builder import QueryBuilder
    criteria = {
        "AND": {
            "fields": ['tweet_text'],
            "operator": "contains",
            "query": "cricket"
        }
    }

    s = QueryBuilder(criteria).search()
    print QueryBuilder.get_raw_query(s)
    for hit in s:
        print hit.tweet_text
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
