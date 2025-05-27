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