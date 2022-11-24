from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Python CI/CD with Github actions"

@app.route("/dev")
def index():
    return "This feature is developed in dev branch"