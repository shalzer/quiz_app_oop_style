#Initialize the question object with text, choices, and answer key
#Check if the selected answer is correct
# Return the correct answer key and its corresponding text

class Question:
    def __init__(self, question_text, choices_dict, answer_key):
        self.question_text = question_text
        self.choices_dict = choices_dict
        self.answer_key =

    def is_correct(self, selected_option):
        return selected_option == self.answer_key

    def get_correct_choice(self):
        return self.answer_key, self.choices_dict[self.answer_key]