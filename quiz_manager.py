 # Loads questions from questions.csv and converts them into Question objects
import csv
from Question import Question

class QuizManager:
    def __init__(self, csv_path="questions.csv"):
        self.csv_path = csv_path                     # Path to CSV file
        self.questions = self.load_questions()       # Load all questions at startup

    def load_questions(self):
        questions = []                               # List to store Question objects

       
        with open(self.csv_path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)               # Reads CSV rows as dictionaries

            for row in reader:
                # Create a Question object from each CSV row
                q = Question(
                    text=row["text"],
                    options=row["options"].split(";"),
                    answer=row["answer"],
                    difficulty=row["difficulty"],
                    category=row["category"],
                    image=row["image"] or None
                )
                questions.append(q)

        return questions                              # Return all loaded questions

    def check(self, user_answer, correct_answer):
        return user_answer == correct_answer          # Returns True if correct
