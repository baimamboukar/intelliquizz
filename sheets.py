from lib2to3.pgen2.token import NUMBER
import gspread
import json

SUBJECT = "ICT"
NUMBER_OF_QUESTIONS = 10
DIFFICULTY = "medium"
TOPIC = "Computer system"
google_credentials = gspread.service_account(filename='credentials.json')
sheet = google_credentials.open_by_key("1L6NurushGZT7vDXeR2v4kMYxxahkdhLkhdmLLROmECY")
worksheet = sheet.worksheet(SUBJECT)
questions = []
data = worksheet.get_all_records()
for question in data:
        if(question["subject"] == SUBJECT and question["level"] == DIFFICULTY):
            questions.append(json.dumps(question))
            if(len(questions) == NUMBER_OF_QUESTIONS):
                break
print(questions)