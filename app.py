import flask
import flask_limiter as lim
import flask_limiter.util as util
import database as db



app = flask.Flask(__name__)
limiter = lim.Limiter(app, key_func=util.get_remote_address)

@app.route("/")
@limiter.limit("100/minute, 1000/hour, 1000/day")
def index():
    test = db.test()
    return flask.render_template("index.html", test=test)


@app.route("/retrieve/<key>")
@limiter.limit("100/minute, 1000/hour, 1000/day")
def retrieve(key):
    ciphertext = db.retrieve(key)
    return flask.render_template("retrieve.html", key=key, ciphertext=ciphertext)
