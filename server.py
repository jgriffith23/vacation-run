from flask import Flask, render_template, session, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import os


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "DEVKEY")
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def show_index():
    """The homepage."""

    return render_template("index.html")


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # connect_to_db(app)

    app.debug = True
    DebugToolbarExtension(app)

    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT)
