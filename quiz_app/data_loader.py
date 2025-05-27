#Import the operating system module to work with file paths
#Load questions
#Check if the file exists; return empty list if not
# Read file content and split into blocks by separator
#Prepare a list to store question data
#loop through each question block and extract information
#Extract question text, choices, and answer key
#Append structured question data to the list
#Skip any improperly formatted blocks
#Return complete list of question

import os
class DataLoader:
    @staticmethod
    def load_questions(file_path):
        if not os.path.exists(file_path):
            return []