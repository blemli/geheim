import flask
import flask_limiter as lim
import flask_limiter.util as util

app = flask.Flask(__name__)
limiter = lim.Limiter(app, key_func=util.get_remote_address)

@app.route("/")
@limiter.limit("100/minute, 1000/hour, 1000/day")
def hello_world():
    return flask.render_template("index.html")

@app.route("/retrieve/<key>")
@limiter.limit("100/minute, 1000/hour, 1000/day")
def retrieve(key):
    pass     #todo: implement
