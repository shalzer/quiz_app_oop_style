#Import the QuizCreator class so we can use it to build a quiz
#This block only runs if this file is executed directly (not imported as a module)
#Start the interactive quiz creation process

from quiz_creator import QuizCreator
if __name__ == "__main__":
    quiz_creator_instance = QuizCreator()
    quiz_creator_instance.start()