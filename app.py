from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    from tweety import Tweety
    Tweety().filter(keywords=['cricket'])
    return 'Welcome to Tweety!'


if __name__ == '__main__':
    app.run()
