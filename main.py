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

@app.route("/teacher-list")
def teacher_list():
    return {"teachers" : ["Sompong", "Somsak", "Danny", "Pannika"]}

@app.route("/list-assignments")
def list_assignments():
    return "This function was created in branch [issue53]"