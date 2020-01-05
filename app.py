from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/map")
def index():
    """Return the homepage."""
    return render_template("map.html")