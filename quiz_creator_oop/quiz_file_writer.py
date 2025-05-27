#Import the Question class so we can accept Question objects as input
#Store filename
#Open the file in append mode ("a") so we add to the end of the file
#Write the question text to the file
#Write each of the multiple choice options (A–D)
#Write the correct answer
#Add separator

from question import Question
class QuizFileWriter:
    def __init__(self, file_name: str = "quiz_data.txt"):
        self.file_name = file_name

    def save_question(self, question: Question):
        with open(self.file_name, "a") as file:
            file.write(f"Question: {question.question_text}\n")
            file.write(f"A) {question.choice_a}\n")
            file.write(f"B) {question.choice_b}\n")
            file.write(f"C) {question.choice_c}\n")
            file.write(f"D) {question.choice_d}\n")
            file.write(f"Answer: {question.correct_answer}\n")
            file.write("-----------------\n")