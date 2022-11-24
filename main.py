from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Python CI/CD with Github actions"

@app.route("/dev")
def index():
    return "This feature is developed in dev branch"

@app.route("/items-list")
def items_list():
    return {"items" : ["A", "B", "C", "D", "E", "F"]}

@app.route("/location")
def location():
    return "We have a nice location for you!"