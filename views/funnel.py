import json
from flask import Blueprint, request
from service.esutil.querybuilder.query_builder import QueryBuilder
from service.commons import json_response

# Register routes blueprint
funnel = Blueprint ('funnel', __name__)

@funnel.route('/', methods=["POST"])
@funnel.route('', methods=["POST"])
def funnel_handler():
    es_size = int(request.args.get('size', 100))
    es_from = int(request.args.get('from', 0))
    data = json.loads(request.data)
    criteria = data.get('criteria')
    sort = data.get('sort')
    s = QueryBuilder(criteria).search(index='tweets_index', doc_type='tweet')
    if sort:
        s = s.sort(*sort)
    s = s[es_from:es_size]
    print "[QUERY]", QueryBuilder.get_raw_query(s)

    try:
        es_res = QueryBuilder.execute(s)
    except Exception as ex:
        res = {
            "status": "error",
            "message": ex.message,
            "args": ex.args
        }
        return json_response(res)
    res = dict()
    if es_res is not None:
        hits = es_res.hits
        res["count"] = {"total": hits.total, "fetched": len(hits.hits) }
        res["results"] = hits.hits
    return json_response(res)