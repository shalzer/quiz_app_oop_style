# Import tkinter for GUI
# Import DataLoader to load questions from file
# Import the main QuizApp GUI class
# Load quiz questions from a file into a list of dictionaries
# If no questions were loaded, print a message and do not start the quiz
# Create the main window for the quiz app
# Pass the window and loaded questions to the QuizApp to start the GUI
# Start the Tkinter event loop to keep the window running
# Entry point: Run the main function when this script is executed

import tkinter as tk
from data_loader import DataLoader
from quiz_app import QuizApp