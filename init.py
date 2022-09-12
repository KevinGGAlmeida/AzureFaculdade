import flask
app = flask.Flask(__name__)

@app.route("/home")
def home():
    return "Flask API get endpoint running"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)