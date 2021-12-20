from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def index():
    return "Here is intelli'Quizz backend!"