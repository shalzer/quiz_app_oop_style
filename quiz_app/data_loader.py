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

        with open(file_path, "r") as file:
            raw_blocks = file.read().strip().split("\n-----------------\n")

        questions = []
        for block in raw_blocks:
            lines = block.strip().split("\n")
            if len(lines) < 6:
                continue

            try:
                question_text = lines[0].split("Question: ")[1]
                choice_texts = [line.split(") ")[1] for line in lines[1:5]]
                answer_key = lines[5].split("Answer: ")[1].strip()

            questions.append({
                "question": question_text,
                "choices": dict(zip("ABCD", choice_texts)),
                "answer": answer_key
            })