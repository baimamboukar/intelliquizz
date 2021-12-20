from flask import Flask
from database.connexion import IntelliquizzDB
from helpers.converters import Converters

import json

app = Flask(__name__)

@app.route("/")
def index():
    intelliDB = IntelliquizzDB()
    db = intelliDB.connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM quizz")
    data = cursor.fetchall()
    objects_list = Converters.convert_questions(data)
    questions = json.dumps(objects_list)
    return questions

@app.route("/anglo_ordinary/<subject>/<number>", )
def anglo_ordinary(subject, number):
    intelliDB = IntelliquizzDB()
    db = intelliDB.connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM quizz WHERE subject = ? LIMIT ?", (subject, number))
    data = cursor.fetchall()
    objects_list = Converters.convert_questions(data)
    return {"results": objects_list}, 200




# cursor.execute(f"INSERT INTO quizz VALUES(6, 'What is flutter ?', 'mobile-dev', 'anglophone', 'advanced', 'Google UIkit for cross-platform mobile apps', 'An open API for meteo - A new operating system - A unicorn India company', 'flutter')")
#     query = "SELECT * FROM quizz"