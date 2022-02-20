from pprint import pprint
from flask import Flask, jsonify
from database.connexion import IntelliquizzDB
from helpers.converters import Converters
import gspread
import json

import json

app = Flask(__name__)

@app.route("/")
def index():
    google_credentials = gspread.service_account(filename='credentials.json')
    sheet = google_credentials.open_by_key("1L6NurushGZT7vDXeR2v4kMYxxahkdhLkhdmLLROmECY")
    worksheet = sheet.worksheet("ICT")
    data = worksheet.get_all_records()
    return jsonify(data)


@app.route("/<subject>/<level>/<number>/" )
def universal(subject,level,number):
    google_credentials = gspread.service_account(filename='credentials.json')
    sheet = google_credentials.open_by_key("1L6NurushGZT7vDXeR2v4kMYxxahkdhLkhdmLLROmECY")
    worksheet = sheet.worksheet(subject)
    questions = []
    data = worksheet.get_all_records()
    matching_dict = list(filter(lambda x: x['subject'] == subject and x['level'] == level, data))
    for question in data:
        if(question["subject"] == subject and question["level"] == level):
            questions.append(question)
            if(len(questions) == number):
                break
        print(type(json.dumps(matching_dict)))
        print(type(jsonify(matching_dict)))
    return {"results": json.dumps(matching_dict)}, 200