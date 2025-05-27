# Initialize a question object with the question text, four choices, and the correct answer
#Store option A, B, C, and D
#Convert the correct answer into upper case and store it
#Check if the correct answer is a valid choice
#Return if true
#Otherwise, return False

class Question:
    def __init__(self, question_text: str, choice_a: str, choice_b: str, choice_c: str, choice_d: str, correct_answer: str):
        self.question_text = question_text
        self.choice_a = choice_a
        self.choice_b = choice_b
        self.choice_c = choice_c
        self.choice_d = choice_d
        self.correct_answer = correct_answer.upper()

    def is_valid_answer(self) -> bool: