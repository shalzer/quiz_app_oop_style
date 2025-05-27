#Import the Question class to create quiz questions
#Import the QuizFileWriter class to handle writing questions to a file
# Create a QuizFileWriter class that will save questions to the given file
#Run the interactive quiz tool
#Greet user
#Start a loop to collect questioms
#Ask user to input question
#Check if the entered correct answer is valid
#Save the answer if valid
#otherwise show an error message
#ask user to if they want to input another question
#if not "yes", end the loop

from question import Question
from quiz_file_writer import QuizFileWriter
class QuizCreator:
    def __init__(self, file_name: str = "quiz_data.txt"):
        self.writer = QuizFileWriter(file_name)

    def start(self):
        print("\n📝 Welcome to Quiz Creator!")
        while True:
            question = self.create_question()
            if question and question.is_valid_answer():
                self.writer.save_question(question)
                print("✅ Question added!")
            else:
                print("❌ Invalid answer. Please try again.")

            add_another_question = input("\nDo you want to add another question? (yes/no): ")
            if add_another_question.strip().lower() != "yes":
                print("✅ Quiz saved!")
                break
    def create_question(self) -> Question:
        question_text = input("Question: ")
        choice_a = input("A.) ")
        choice_b = input("B.) ")
        choice_c = input("C.) ")
        choice_d = input("D.) ")
        correct_answer = input("Correct answer (A/B/C/D): ").strip()
        return Question(question_text, choice_a, choice_b, choice_c, choice_d, correct_answer)