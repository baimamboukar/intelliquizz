class Question:
    def __init__(self, id, label, subject, section, level, correct_answer, wrong_answers, topic):
        self.id = id
        self.label = label
        self.subject = subject
        self.section = section
        self.level = level
        self.correct_answer = correct_answer
        self.wrong_answers = wrong_answers
        self.topic = topic
    def __str__(self):
        return f"Question: {self.label} - {self.subject} - {self.section} - {self.level} - {self.correct_answer} - {self.wrong_answers} - {self.topic}"
    def toJSON(self):
        return {
            'id': self.id,
            'label': self.label,
            'subject': self.subject,
            'section': self.section,
            'level': self.level,
            'correct_answer': self.correct_answer,
            'wrong_answers': self.wrong_answers,
            'topic': self.topic
        }
    def fromJSON(self, json):
        self.id = json['id']
        self.label = json['label']
        self.subject = json['subject']
        self.section = json['section']
        self.level = json['level']
        self.correct_answer = json['correct_answer']
        self.wrong_answers = json['wrong_answers']
        self.topic = json['topic']
        return self