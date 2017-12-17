from flask import Flask, request

app = Flask(__name__)

from views.funnel import funnel
app.register_blueprint (funnel, url_prefix='/funnel')

@app.route('/')
def index():
    return '<h1>Welcome to Tweety!</h1>'

@app.route('/stream')
def stream_event():
    from service.commons import json_response
    res = dict()
    try:
        keywords = request.args.get('keywords')
        if keywords:
            keywords = keywords.split(",")
        else:
            res = {
                "status": "error",
                "message": "Please provide a few keyword(s) (comma-separated)",
                "example": "/stream?keywords=kw1,kw2,abc,xyz"
            }
            return json_response(res)
        from tweety import Tweety
        Tweety().filter(keywords=keywords)
        res['status'] = "success"
        res['message'] = "Started streaming tweets with keywords {}".format(keywords)

    except Exception as exc:
        res['status'] = "error"
        res['message'] = exc.message
        res['args'] = exc.args
    return json_response(res)

if __name__ == '__main__':
    app.run()
