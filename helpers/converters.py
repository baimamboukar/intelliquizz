from models.question import Question
import pprint
class Converters:
    @staticmethod
    def convert_questions(questions):
        """
        Convert questions to a format that can be used by the
        neural network.
        """
        converted_questions = []
        for question in questions:
            question_object = Question(question[0], question[1], question[2], question[3], question[4], question[5], question[6], question[7])
            converted_questions.append(question_object.toJSON())
        return converted_questions