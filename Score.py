import os
from Utils import *

def clean_score_file():
    if os.path.exists("Scores.txt"):
        os.remove("Scores.txt")

def add_score(difficulty):
    new_score = int(difficulty) * 3 + 5
    try:
        with open("Scores.txt", "r") as file:
            current_score = int(file.read())
    except FileNotFoundError:
        current_score = 0

    total_score = current_score + new_score
    with open("Scores.txt", "w") as file:
        file.write(str(total_score))