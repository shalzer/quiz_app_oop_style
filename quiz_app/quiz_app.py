# Import Question class (must support dict input)
# Convert each dictionary in question_data into a Question object
# Initialize the score and total number of questions
# Style settings for consistent UI appearance
#set up widgets
# Load the first question to begin the quiz
# Set up the main window's title, size, and background color
# Title label at the top of the app
# Label to display the current score
# Label to show the question text
# Create four buttons (A–D) for answer choices
# Label to display whether the user's answer is correct or not
# Button to go to the next question (disabled until a question is answered)
# If there are no more questions left, show the final score
# Randomly select the next question and remove it from the list
# Display the question text
# Update the answer buttons with the new choices and enable them
# Clear previous result and update the score display
# Check if the selected answer is correct
# If incorrect, show the correct answer
# Disable all answer buttons so the user can't change their answer
# Update the score display and enable the "Next Question" button
# Display a completion message and the final score
# Disable all buttons so the quiz is fully finished

import tkinter as tk
import random
from question import Question
class QuizApp:
    def __init__(self, window, question_data):
        self.window = window
        self.questions_list = [Question(data["question"], data["choices"], data["answer"]) for data in question_data]
        self.score = 0
        self.total_questions = len(self.questions_list)
        self.style_options = {"font": ("Roboto", 12, "bold"), "bg": "#0f172a", "fg": "white"}

        self.setup_ui()
        self.load_next_question()

    def setup_ui(self):
        self.window.title("🎮 QUIZ APP")
        self.window.geometry("600x550")
        self.window.configure(bg="#0f172a")

        tk.Label(self.window, text="⚔️ Test Your Skills!", font=("Roboto", 20, "bold"),
                 bg="#0f172a", fg="#facc15", pady=10).pack()

        self.score_label = tk.Label(self.window, **self.style_options)
        self.score_label.pack()

        self.question_label = tk.Label(self.window, font=("Roboto", 14, "bold"),
                                       fg="#e0e0e0", bg="#0f172a", wraplength=550, pady=20)
        self.question_label.pack()

        self.answer_buttons = {}
        for option in "ABCD":
            self.answer_buttons[option] = tk.Button(
                self.window, width=50, bg="#1e293b", fg="white",
                activebackground="#f43f5e", activeforeground="white",
                relief="groove", borderwidth=3, font=self.style_options["font"],
                command=lambda opt=option: self.evaluate_answer(opt)
            )
            self.answer_buttons[option].pack(pady=6)

        self.result_label = tk.Label(self.window, font=("Roboto", 14, "bold"),
                                     bg="#0f172a", fg="white")
        self.result_label.pack(pady=20)

        self.next_button = tk.Button(self.window, text="➡️ Next Question", font=self.style_options["font"],
                                     bg="#3b82f6", fg="white", activebackground="#2563eb",
                                     state="disabled", command=self.load_next_question)
        self.next_button.pack(pady=10)

    def load_next_question(self):
        if not self.questions_list:
            self.display_final_score()
            return

        self.current_question = random.choice(self.questions_list)
        self.questions_list.remove(self.current_question)

        self.question_label.config(text=self.current_question.question_text)
        for key, value in self.current_question.choices_dict.items():
            self.answer_buttons[key].config(text=f"{key}) {value}", state="normal")

        self.result_label.config(text="")
        self.score_label.config(text=f"Score: {self.score} / {self.total_questions}")
        self.next_button.config(state="disabled")