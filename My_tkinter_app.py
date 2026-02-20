# My Tkinter quiz application with category selection, difficulty filtering,
# image support, correct/wrong answer messages, and Next button flow.

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
import os
import random
from quiz_manager import QuizManager



class CategoryDifficultySelector:
    def __init__(self, root, start_quiz_callback):
        self.root = root
        self.start_quiz_callback = start_quiz_callback
        self.root.title("Choose Quiz Settings")
        self.root.configure(bg="#32CD32")  # Green background for accessibility

        # Title label
        tk.Label(root, text="Select Category", font=("Arial", 16, "bold"),
                 bg="#32CD32").pack(pady=10)

        # Radio buttons for category selection
        self.category_var = tk.StringVar()
        categories = ["EA Basics", "Flooding", "Pollution", "Regulation"]
        for cat in categories:
            tk.Radiobutton(root, text=cat, variable=self.category_var, value=cat,
                           bg="#32CD32", font=("Arial", 14)).pack(anchor="w")

        # Difficulty label
        tk.Label(root, text="Select Difficulty", font=("Arial", 16, "bold"),
                 bg="#32CD32").pack(pady=10)

        # Radio buttons for difficulty selection
        self.difficulty_var = tk.StringVar()
        difficulties = ["Easy", "Medium", "Hard"]
        for diff in difficulties:
            tk.Radiobutton(root, text=diff, variable=self.difficulty_var, value=diff,
                           bg="#32CD32", font=("Arial", 14)).pack(anchor="w")

        # Start button
        tk.Button(root, text="Start Quiz", font=("Arial", 14),
                  command=self.start).pack(pady=20)

    def start(self):
        # Validate user selections
        category = self.category_var.get()
        difficulty = self.difficulty_var.get()

        if not category or not difficulty:
            messagebox.showerror("Error", "Please select both category and difficulty")
            return

        # Close selector and launch quiz
        self.root.destroy()
        self.start_quiz_callback(category, difficulty)



# MAIN QUIZ 

class TkQuizApp:
    def __init__(self, root, category, difficulty):
        self.root = root
        self.root.title("EA Hybrid Quiz")
        self.root.configure(bg="#32CD32")  # Green background for accessibility

        # Load questions from CSV
        self.qm = QuizManager()

        # Filter questions by category and difficulty
        self.questions = [
            q for q in self.qm.questions
            if q.category == category and q.difficulty == difficulty
        ]

        # Randomly select 5 questions
        self.questions = random.sample(self.questions, min(5, len(self.questions)))

        self.q_index = 0  # Tracks current question index
        self.score = 0    # Tracks correct answers

        # Question text label
        self.question_label = tk.Label(root, wraplength=500, font=("Arial", 16),
                                       bg="#32CD32")
        self.question_label.pack(pady=10)

        # Image display label
        self.image_label = tk.Label(root, bg="#32CD32")
        self.image_label.pack(pady=10)

        # Dropdown for answer choices
        self.answer_var = tk.StringVar()
        self.dropdown = ttk.Combobox(root, textvariable=self.answer_var,
                                     state="readonly", font=("Arial", 14))
        self.dropdown.pack(pady=5)

        # Submit button
        self.submit_button = tk.Button(root, text="Submit", font=("Arial", 14),
                                       command=self.submit_answer)
        self.submit_button.pack(pady=5)

        # Next button (disabled until Submit is pressed)
        self.next_button = tk.Button(root, text="Next", font=("Arial", 14),
                                     command=self.next_question, state="disabled")
        self.next_button.pack(pady=5)

        # Load the first question
        self.load_question()

   
    def load_question(self):
        # End quiz if no more questions
        if self.q_index >= len(self.questions):
            messagebox.showinfo("Quiz Complete",
                                f"Score: {self.score}/{len(self.questions)}")
            self.root.destroy()
            return

        q = self.questions[self.q_index]  # Current question object

        # Display question text
        self.question_label.config(text=q.text)

        # Load answer choices into dropdown
        self.dropdown["values"] = q.options
        self.answer_var.set(q.options[0])

        # Load image if available
        if q.image:
            img_path = os.path.join("images", q.image)
            if os.path.exists(img_path):
                self.img = PhotoImage(file=img_path)
                self.image_label.config(image=self.img)
            else:
                self.image_label.config(image="")
        else:
            self.image_label.config(image="")

        # Reset buttons for new question
        self.submit_button.config(state="normal")
        self.next_button.config(state="disabled")

    
    def submit_answer(self):
        q = self.questions[self.q_index]        # Current question
        user_answer = self.answer_var.get()     # User's selected answer

        # Correct answer feedback
        if self.qm.check(user_answer, q.answer):
            messagebox.showinfo("Correct", "Well done! That is the correct answer.")
            self.score += 1
        else:
            # Wrong answer feedback with correct answer shown
            messagebox.showwarning(
                "Incorrect",
                f"That is not correct.\n\nCorrect answer: {q.answer}"
            )

        # Disable Submit to prevent answer changes
        self.submit_button.config(state="disabled")

        # Enable Next to move forward
        self.next_button.config(state="normal")

    
    def next_question(self):
        self.q_index += 1  # Move to next question
        self.load_question()



def launch_quiz(category, difficulty):
    quiz_root = tk.Tk()  # Create quiz window
    TkQuizApp(quiz_root, category, difficulty)
    quiz_root.mainloop()






