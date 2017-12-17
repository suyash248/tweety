import json
from flask import Blueprint, request
from service.esutil.querybuilder.query_builder import QueryBuilder
from service.commons import json_response

# Register routes blueprint
funnel = Blueprint ('funnel', __name__)

@funnel.route('/', methods=["POST"])
@funnel.route('', methods=["POST"])
def funnel_handler():
    data = json.loads(request.data)
    criteria = data.get('criteria')
    sort = data.get('sort')
    s = QueryBuilder(criteria).search()
    print "[QUERY]", QueryBuilder.get_raw_query(s)

    es_res = QueryBuilder.execute(s)
    res = {"error": "Error occurred"}
    if es_res is not None:
        hits = es_res.hits
        res = {
            "count": hits.total,
            "results": hits.hits
        }
    return json_response(res)