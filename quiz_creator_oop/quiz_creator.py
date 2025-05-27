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
