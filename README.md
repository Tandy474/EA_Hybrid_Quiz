


# EA Hybrid Quiz

## 1  Introduction
The Environment Agency(EA) operates across a wide range of environmental, regulatory, and operational domains, including flood risk management, pollution response, permitting, environmental monitoring, and incident management.  Staff and delivery partners must maintain a consistent baseline knowledge to ensure safe, compliant, and effective operations.  This includes understanding EA policies, procedures, environmental principles, and technical concepts relevant to decision-making.  In such a multidisciplinary environment, accessible digital learning tools play an important role in supporting competence, onboarding, and continuous professional development.

The EA Hybrid Quiz is an interactive learning application designed to strengthen staff understanding of key EA Topics.  The tool provides a structured quiz experience that can be used for training, induction, toolbox talks, or self-directed e-learning.  The (MVP) minimum viable product includes a login system, category and difficulty selection, question presenting optional answer validation, and instant feedback.  The quiz content can cover EA Basics, Flooding, Pollution, Regulation, or mathematical knowledge relevant to EA roles.

A key feature of this project is the hybrid interface approach, offering two front-end options:
  TKinter: a desktop-style GUI suitable for local use on EA laptops.
  Streamlit: a browser-based interface ideal for demonstrations, remote access, and rapid deployment.

Both interfaces read from the same CSV-based data store, ensuring consistency and ease of maintenance.  The project uses Python and object-oriented programming principles, with classes for questions, quiz management, and authentication.  The system includes exception handling, input validation, and testable logic, supported by automated unit tests.

For the EA, this MVP is relevant because it provides a low-cost, accessible, and easily maintainable tool that supports organisational competence. The Hybrid design also demonstrates modern development practices, version control, documentation, and continuous integration, aligning with professional software engineering standards.


## 2  Design Section
### Figma-style GUI design
<img width="931" height="772" alt="image" src="https://github.com/user-attachments/assets/f11d80de-d61f-4363-982a-37f248ced35d" />

Figma is a collaborative interface-design tool used to create wireframes, mockups, and interactive prototypes.
Designers use it to plan screen layouts, colours, typography, and other user journeys before coding begins.

For the EA HYbrid Quiz, Figma was used to sketch each screen i.e. (_Login_, _Welcome_, _Category Selection_, _Quiz_) to ensure accessibility  and usability requirements are met in line with EA digital principles.

## Requirements Table


### Functional Requirements Table
| ID   | Requirement |
| ---- | ----- |
| FR1  | System must authenticate users via CSV.  |
| FR2  | System must allow category selection.  |
| FR3  | System must allow difficulty selection.  |
| FR4  | System must load questions from CSV.  |
| FR5  | System must display questions and options.  |
| FR6  | System must validate answers.  |
| FR7  | System must show correct/ incorrect feedback.  |
| FR8  | System must show final score.  |
| FR9  | System must support both TKinter and Streamlit interfaces  |



### Accessibility Requirements Table
| ID   | Requirement |
| ---- | -------- |
| AR1  | High-contrast colour scheme. (e.g., white text on blue/green backgrounds) |
| AR2  | Keyboard navigation supported.  |
| AR3  | Text-based feedback(not colour only. |
| AR4  | Large readable fonts.  |
| AR5  | Clear error messages.  |

These choices support inclusive use by EA staff and delivery partners with diverse needs.


### Non-Functional Requirements Table
| ID   | Requirement |
| ---- | -------- |
| NFR1 | App should load within 2 seconds.  |
| NFR2 | CSV errors handled.  |
| NFR3 | Code must be modular and maintainable.  |
| NFR4 | Logic must be testable via unit tests.  |
| NFR5 | Must run on standard EA laptops without extra installation.  |



## Tech Stack Outline
  **Language:** Python 3
  
  **GUI Frameworks:**
      +TKinter (desktop)
      +Streamlit (Web)
  
**Data Storage:** (CSV files)

**Libraries:**
    +CSV - reading/writing data
    + TKinter - GUI
   + Streamlit - Web interface
   + unittest - automated testing
   + dataclasses - Question model
    
**Tools:**
   + GitHub - version control
   + Figma -  interface prototyping
   + Streamlit - Web interface
   + VS Code - development environment
    
 ## Code design document   
  ### Class diagrams
<img width="642" height="705" alt="image" src="https://github.com/user-attachments/assets/989315fd-90de-4898-8edd-7567e2658afa" />

The UML  class diagrams provide a visual representation of the system's structure, showing classes, their attributes and methods, and the relationship between them. In the EA Hybrid Quiz, the class diagram clarifies how _LoginManager_, _QuizManager_, _Question_, _LoginWindow_, _TKQuizApp_, and the _Streamlit interface_ collaborate, supporting modularity, testability, and maintainability.


## 3 Development Section
 
The EA Hybrid Quiz was developed using Python and follows a modular object-oriented structure.  The system is divided into logical components, data models, managers, and user interfaces to ensure maintainability, testability, and clarity.  This section explains the main modules and functions, showing how they work together to deliver the full quiz experience.


### 3.1 Question (Question.py)
The _Question_ class represents a single question.  It stores the text, answer options, correct answer, difficulty, and category 

 #Defines a simple Question object to store each quiz question
    from dataclasses import dataclass
    from typing import List, Optional

    @dataclass
    class Question:
         text: str                 # The question text
         options: List[str]        # List of answer choices
         answer: str               # Correct answer
         difficulty: str           # Difficulty level
         category: str             # Category (EA Basics, Flooding, etc.)
        image: Optional[str] = None  # Optional image filename

How the _Question_ contributes to the system:
+ Provides a structured data model for each question.
+ Ensures consistency when loading questions from _CSV_
+ Supports both TKinter and Streamlit interfaces with the same format.


### 3.2 QuizManager(quiz_manager.py)
_QuizManager_ handles loading questions from _CSV_ and checking answers.
It can be used and reused by TKinter and Streamlit.
```
 #Loads questions from questions.csv and converts them into Question objects
          
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
         #Create a Question object from each CSV row
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
```



How it contributes
  + Loads data (FR2) from _CSV_
  + Converts raw CSV rows into _Question_
  + Provides a function (check) for unit testing
  + Ensure separation of concerns: logic stays out of GUI.


### 3.3 LoginManager (login_Manager.py)
The LoginManager handles user authentication _users.csv_
``` 
  #user authentication by checking users.csv

    import csv
    class LoginManager:
        def __init__(self, csv_path="users.csv"):
           self.csv_path = csv_path                     # Path to users CSV
           self.users = self.load_users()               # Load all users

      def load_users(self):
          users = {}                                   #  username → password
          with open(self.csv_path, "r", encoding="utf-8-sig") as f:
             reader = csv.DictReader(f)
             for row in reader:
                users[row["username"]] = row["password"]
        return users

     def authenticate(self, username, password):
        return username in self.users and self.users[username] == password
```

 How it contributes
   + Implements secure login (FR1)
   + Provides clear error handling for invalid credentials.
   + Keeps authentication separate from UI logic.


### 3.4 TKinter Interface (My_TKinter_app.py)
The TKinter provides a desktop-style GUI for EA laptops
```
#My Tkinter quiz application with category selection, difficulty filtering,
#image support, correct/wrong answer messages, and Next button flow.


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

        #Title label
        
           tk.Label(root, text="Select Category", font=("Arial", 16, "bold"),
                   bg="#32CD32").pack(pady=10)

        #Radio buttons for category selection
        
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

        #Start button
        tk.Button(root, text="Start Quiz", font=("Arial", 14),
                  command=self.start).pack(pady=20)

      def start(self):
        #Validate user selections
        category = self.category_var.get()
        difficulty = self.difficulty_var.get()

        if not category or not difficulty:
            messagebox.showerror("Error", "Please select both category and difficulty")
            return

        #Close selector and launch quiz
         self.root.destroy()
         self.start_quiz_callback(category, difficulty)

 MAIN QUIZ 

    class TkQuizApp:
       def __init__(self, root, category, difficulty):
          self.root = root
          self.root.title("EA Hybrid Quiz")
          self.root.configure(bg="#32CD32")  # Green background for accessibility

        #Load questions from CSV
         self.qm = QuizManager()

        #Filter questions by category and difficulty
          self.questions = [
             q for q in self.qm.questions
             if q.category == category and q.difficulty == difficulty
        ]

        #Randomly select 5 questions
         self.questions = random.sample(self.questions, min(5, len(self.questions)))

         self.q_index = 0  # Tracks current question index
         self.score = 0    # Tracks correct answers

        #Question text label
          self.question_label = tk.Label(root, wraplength=500, font=("Arial", 16),
                                       bg="#32CD32")
          self.question_label.pack(pady=10)

        #Image display label
          self.image_label = tk.Label(root, bg="#32CD32")
          self.image_label.pack(pady=10)

        #Dropdown for answer choices
          self.answer_var = tk.StringVar()
          self.dropdown = ttk.Combobox(root, textvariable=self.answer_var,
                                     state="readonly", font=("Arial", 14))
          self.dropdown.pack(pady=5)

        #Submit button
          self.submit_button = tk.Button(root, text="Submit", font=("Arial", 14),
                                       command=self.submit_answer)
          self.submit_button.pack(pady=5)

        #Next button (disabled until Submit is pressed)
          self.next_button = tk.Button(root, text="Next", font=("Arial", 14),
                                     command=self.next_question, state="disabled")
          self.next_button.pack(pady=5)

        #Load the first question
          self.load_question()

     def load_question(self):
        #End quiz if no more questions
         if self.q_index >= len(self.questions):
            messagebox.showinfo("Quiz Complete",
                                f"Score: {self.score}/{len(self.questions)}")
            self.root.destroy()
            return

        q = self.questions[self.q_index]  # Current question object

        #Display question text
         self.question_label.config(text=q.text)

        #Load answer choices into dropdown
         self.dropdown["values"] = q.options
         self.answer_var.set(q.options[0])

        #Load image if available
         if q.image:
            img_path = os.path.join("images", q.image)
            if os.path.exists(img_path):
                self.img = PhotoImage(file=img_path)
                self.image_label.config(image=self.img)
            else:
                self.image_label.config(image="")
        else:
            self.image_label.config(image="")

        #Reset buttons for new question
         self.submit_button.config(state="normal")
         self.next_button.config(state="disabled")

     def submit_answer(self):
         q = self.questions[self.q_index]        # Current question
         user_answer = self.answer_var.get()     # User's selected answer

        #Correct answer feedback
         if self.qm.check(user_answer, q.answer):
            messagebox.showinfo("Correct", "Well done! That is the correct answer.")
            self.score += 1
        else:
            # Wrong answer feedback with correct answer shown
            messagebox.showwarning(
                "Incorrect",
                f"That is not correct.\n\nCorrect answer: {q.answer}"
            )

        #Disable Submit to prevent answer changes
         self.submit_button.config(state="disabled")

        #Enable Next to move forward
         self.next_button.config(state="normal")

     def next_question(self):
        self.q_index += 1  # Move to next question
        self.load_question()

     def launch_quiz(category, difficulty):
        quiz_root = tk.Tk()  # Create quiz window
        TkQuizApp(quiz_root, category, difficulty)
        quiz_root.mainloop()
```

How it contributes
  + Provides a fully interactive GUI (FR1 -FR9)
  + Uses accessible colours, large fonts, and clear feedback (AR1 -AR5)


### 3.5 Streamlit Interface (streamlit_app.py)

Streamlit provides a browser-based interface with built-in accessibility features such as responsive layout, keyboard navigation, and screen-reader compatibility.

```
      import streamlit as st
      import random
      from quiz_manager import QuizManager
      from login_manager import LoginManager

      qm = QuizManager()      # handles questions and answers
      lm = LoginManager()     # handles login authentication
    
     def main():
      #Track login state
       if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    #Login screen
       if not st.session_state.logged_in:
        username = st.text_input("Username")                     # user enters name
        password = st.text_input("Password", type="password")    # hidden password field

        if st.button("Login") and lm.authenticate(username, password):
            st.session_state.logged_in = True                    # mark user as logged in
            st.experimental_rerun()                              # reload quiz screen
        return

       st.title("EA Hybrid Quiz")

    #Initialise score and question counter
    
       if "score" not in st.session_state:
        st.session_state.score = 0                               # number of correct answers
        st.session_state.q_count = 0                             # how many questions asked

    #Create a shuffled list of 5 unique questions
       if "question_list" not in st.session_state:
        st.session_state.question_list = random.sample(qm.questions, 5)

    #End of quiz
       if st.session_state.q_count >= 5:
        st.success(f"Score: {st.session_state.score}/5")         # show final score

        #Play Again button resets everything
        if st.button("Play Again"):
            st.session_state.score = 0
            st.session_state.q_count = 0
            st.session_state.question_list = random.sample(qm.questions, 5)
            st.experimental_rerun()
        return

    #Get next question in the shuffled list
       q = st.session_state.question_list[st.session_state.q_count]

    #Display question and options
       choice = st.radio(q.text, q.options)                         # user selects an answer

    #Submit button checks answer
       if st.button("Submit"):
        if qm.check(choice, q.answer):                           # compare user answer
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect. Correct answer: {q.answer}")

          st.session_state.q_count += 1                            # move to next question
          st.experimental_rerun()                                  # refresh page
    main()
```


How it contributes
+ Automatically handles layout accessibility
+ Ideal for remote training or demonstrations.
+ Provides a web-based alternative interface.


### 3.6  Application Entry Point (main.py)


#Controls the login flow, welcome screen, and launches the quiz

```
       import tkinter as tk
       from tkinter import messagebox
       from login_manager import LoginManager
       from My_tkinter_app import CategoryDifficultySelector, launch_quiz
#LOGIN WINDOW 
      class LoginWindow:
      def __init__(self, root):
          self.root = root
          self.root.title("EA Quiz Login")
           self.root.configure(bg="#1E90FF")  # Blue background

          self.lm = LoginManager()           # Load users.csv

        #Username label + entry
        tk.Label(root, text="Username", bg="#1E90FF", fg="white", font=("Arial", 12)).pack(pady=5)
        self.username_entry = tk.Entry(root, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        #Password label + entry
        tk.Label(root, text="Password", bg="#1E90FF", fg="white", font=("Arial", 12)).pack(pady=5)
        self.password_entry = tk.Entry(root, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        #Login button
        tk.Button(root, text="Login", font=("Arial", 12), command=self.try_login).pack(pady=10)

    #Validate login credentials
      def try_login(self):
          username = self.username_entry.get()
          password = self.password_entry.get()

       if self.lm.authenticate(username, password):
            self.root.destroy()
            self.open_welcome()
      else:
            messagebox.showerror("Login Failed", "Incorrect username or password")
            
        #WELCOME SCREEN 
      def open_welcome(self):
         welcome = tk.Tk()
         welcome.title("Welcome")
         welcome.configure(bg="#32CD32")  # Green background


        #Welcome message
         tk.Label(
            welcome,
            text="Welcome to the EA Hybrid Quiz!",
            bg="#32CD32",
            fg="white",
            font=("Arial", 16, "bold")
        ).pack(pady=20)
        #Continue button
          tk.Button(
            welcome,
            text="Continue",
            font=("Arial", 14),
            command=lambda: self.open_category_screen(welcome)
        ).pack(pady=20)


        welcome.mainloop()
    #Open category/difficulty selector
     def open_category_screen(self, win):
           win.destroy()
          selector_root = tk.Tk()
          CategoryDifficultySelector(selector_root, launch_quiz)
          selector_root.mainloop()
#START APP
if __name__ == "__main__":
      root = tk.Tk()
      LoginWindow(root)
      root.mainloop()
```

How it contributes
  + Controls the full journey
  + Ensures a clean transition between login -- selection -- quiz
  + Supports accessibility by ensuring predictable navigation(AR2)


## 3.7 How all components work together
+ 1 User opens app Main.py   _launches login window.
+ 2 LoginManager authenticates credentials  _user proceeds_
+ 3 QuizManager loads questions   _filters by category/difficulty_.
+ 4 Tkinter or Streamlit displays questions  _user interacts._
+ 5 QuizManager.check() validates answers   _accessible feedback shown._
+ Final score is displayed    _quiz ends._


## 4 Testing Section
Testing was an essential part of developing the EA Hybrid Quiz, ensuring that the system behaved reliably, met functional requirements, and remained accessible to EA staff.  A combination of manual testing and automated unit testing was used to validate both the graphical interfaces (TKinter and Streamlit) and the underlying logic.  This blended approach ensured that the application was tested from both a user experience and code quality perspective.

### 4.1 Testing strategy and methodology
A systemic and strategic testing approach was adopted, combining two complementary methods.

### 4.1.1 Manual testing (GUI focused)
Manual testing was to validate:
  + User interactions with both TKinter and Streamlit
  + Navigation between screens
  + Accessibility features (high contrast, readable fonts, keyboard navigation)
  + Error message and input validation
  + CSV loading behaviour
  + Display image
  + End of quiz and scoring


### 4.1.2 Automatic unit testing (logic focused)
Automated tests were written using Python's built-in _unittest_ frameworks.  These tests focused on:
+ Pure functions such as _QuizManager.check()_
+ CSV loading (smoke test)
+ Ensuring the question bank loads correctly.

Unit testing ensured that the core logic remained stable as features were added incrementally.  This supports future continuous integration pipelines.


### 4.1.3 Why this strategy was chosen

| Method           | Purpose                                                  | Justification                                                                 |
| :---             | :---:                                                    |  --:                                                                          |
| Manual Testing   | Validate GUI behaviour, accessibility, and user flow     | GUI requires human interaction to verify layout, readability, and usability   |
| Unit testing     | Validate logic, ensure reliability, prevent regressions  | Pure function and data loading can be tested automatically and repeatedly     |


### 4.2 Outcomes of application testing
### 4.2.1 Manual testing results
The table below summarises the outcomes of manual tests performed on both TKinter and Streamlit versions.


| Test Case                         | Expected Result                     | Actual Result         |Pass/Fail |
| :---                              | :---:                               | ---:                  | ---:     |
| Login with valid credentials      |User proceeds to welcome screen      | Works as expected     |  Pass    |
| Login with invalid credentials    | Error message displayed             | Error clearly shown   |  Pass    |           
|Category selection                 | User must select a category         |Error shown if mssing  |  Pass    |           
| Difficuly selection               | User must select difficulty         | Error shown if missing|  Pass    |           
| Question loads correclty          | Text, options, appear               | All elements load     |  Pass    |           
| Submit correct answer             | "Correct" feedback dsplayed         | Works                 |  Pass    |           
| Submit incorrect answer           | Incorrect answer is popup           | Works                 |  Pass    |           
| Next button diasabled until submit| Prevents skipping                   | Works                 |  Pass    |           
| End Quiz score                    | Score displayed accurately          | Works                 |  Pass    |           
| TKinter image loading             |Image displayed if available         | Works                 |  Pass    |           

All manual tests passed successfully, demonstrating that the GUI behaves consistently and meets functional and accessibility requirements.

### 4.2.2 Unit testing outcomes
Unit tests were executed using:
  _python m unittest_
```
###  Unit test code (test_quiz.py) 
     import unittest
     from quiz_manager import QuizManager
#SMOKE TEST: ensures the QuizManager loads without crashing

     class TestSmoke(unittest.TestCase):
         def test_quiz_manager_loads(self):
            qm = QuizManager()   # Should not raise any exceptions
            self.assertIsNotNone(qm.questions)  # Questions list should exist
            self.assertGreater(len(qm.questions), 0)  # Should load at least 1 question

#LOGIC TESTS: ensures answer checking works correctly
   class TestQuizLogic(unittest.TestCase):
      def test_check_correct(self):
        qm = QuizManager()
        self.assertTrue(qm.check("A", "A"))  # Same answer → True

     def test_check_incorrect(self):
        qm = QuizManager()
        self.assertFalse(qm.check("B", "A"))  # Different answer → False
#RUN ALL TESTS
  if __name__ == "__main__":
    unittest.main()

```
<img width="505" height="117" alt="image" src="https://github.com/user-attachments/assets/6cff7e87-9de4-4fa8-bdb6-8d998939c561" />


This demonstrates that:
  + The logic behaves predictably
  +  The question bank loads correctly
  + The answer checking function works as intended

###  Summary of testing outcomes
  + All manual tests passed, confirming that the GUI behaves correctly
  + All unit tests passed, confirming that the core logic is stable and reliable.
  + The testing strategy successfully validated both the user experience and the logic, ensuring a suitable MVP for EA staff training.


##  5 Documentation Section
### 5.1 User documentation for (EA)

The EA Hybrid Quis has been designed to be simple, accessible, and intuitive for the Environments agency staff.  This section explains how to interact with the quiz, whether using the desktop (TKinter) version or the browser (Streamlit) version.

### Getting started

### Using the TKinter desktop version.
  1.  Open the project folder on your EA laptop
  2.  Run the application by double-clicking:
         + _main.py_
         + _python main.py_
  4.  The login window will appear automatically

### Using the Streamlit Web version
  1.  Open a terminal in the project folder
  2.  Run:
      + streamlit run streamlit_app.py
  3.  Your default browser will open the quiz interface.

### Logging In
  1.  Enter your EA username and password (stored in _users.csv_)
  2.  Select Login.
  3.  If the credentials are incorrect, an accessible error message will appear.
      This ensures only authorised staff can access the quiz.

### Selecting a Quiz
After logging in:
  1.  Choose a category (e.g., EA Basic, Flooding, Pollution, Regulation).
  2.  Choose a difficulty level (Easy, Medium, Hard)
  3.  Select Start Quiz.
      If either selection is missing, the system will display a clear error message.

### Answering Questions
  1.  Read the question text
  2. Select your answer
        + Tkinter:  _dropdown menu_
        + Streamlit : _radio buttons_
  3. Select Submit
      You will receive immediate feedback:
        + Correct: green success message.
        + Incorrect: message showing the correct answer
         +  Feedback is text-based to support accessibility.

### Navigating the Quiz
* Select Next to move to the next question
* You cannot change your answer once submitted
* The quiz continues until all questions are completed.

### Finishing the Quiz
At the end, your score is displayed:
  + Quiz Complete!
  + Your Score: X/5
  + You can then close the application.

### 5.2 Technical Documentation (for Developers)
This section explains how to run tests locally, understand the project structure, and interpret the main components of the codebase.

### Project Structure

EA_Hybrid_Quiz
  README.md
  
 + main.py                      # Entry point for Tkinter version
 
 + My_tkinter_app.py            # Tkinter GUI implementation
  
+ streamlit_app.py               # Streamlit web interface
 
 + quiz_manager.py              # Core quiz logic (loading questions, checking answers)
  
+ login_manager.py             # Authentication logic
 
 + Question.py                  # Dataclass model for questions
 

 tests
  + __init__.py
  + test_quiz.py             # Unit tests
  + questions.csv            # Quiz data
  + users.csv                # Login credentials

This modular structure separates logic, data, and interface layers, making the system easier to maintain and extend.

##  Running tests locally
The project uses Python's built-in _unittest_ framework.

###  Run all tests
From the project root:
_python -m unittest_

### 5.3  Understanding the codebase
###  5.3.1 Question Model (_Question.py_)
Defines the structure of the quiz question using a dataclass.  This ensures consistent handling of question text, options, answers, difficulty, and category

###  5.3.2 QuizManager (_Quiz_manager.py_)
Handles:
* Loading questions from CSV
* Converting rows into _Question_
* Checking whether a user's answer is correct

###  5.3.3 LoginManager (_Login_manager.py_)
+ Loads usernames and passwords from _users.csv_ and validates login attempts.
+ This keeps authentication logic separate from GUI.

###  5.3.4 TKinter GUI (_My_tkinter_app.py_)
Implements the desktop interface:
+ Dropdown answer selection
+ Image display
+ Accessible feedback
+ Navigation between questions
  This is designed with EA accessibility principle in mind.

###  5.3.5 Streamlit GUI (_streamlit_app.py_)
Implements the browser-based interface:
+ Radio button answer selection
+ Automatic layout and accessibility (ideal for remote or web-based use)

## 6 Evaluation Section
The development of the EA Hybrid Quiz was an insightful process, reflecting on its highlights of the MVP of the final product and the areas where further refinement would have strengthened the outcome.  The project followed a full project software-development lifecycle, from early prototyping in Figma to implementation, testing, and documentation.  This section evaluates what went well, what could have been improved and how the experience contributes to future development practice. 


###  6.1 What went well
Several aspects of the project progressed smoothly and contributed to a stable and  accessible, and maintainable product.

  + ### Clear modular architecture
  Separating the system into _QuizManager,_ _LoginManager,_  _Question,_  and two independent interfaces _(TKinter and Streamlit)_ made the codebase easier to understand and extend.  This approach aligns with widely accepted software-engineering principles such as separation of concerns and modularity, as described in the [https://PythonSoftwareEngineering Guidelines](https://peps.python.org/pep-0008).

* ###  Effective use of prototyping tools
  Creating early wireframes in Figma helped to map out the user journey and identify accessibility considerations before coding began.  This reduced rework and ensured the interface aligned with EA accessibility expectations.  Figma's collaborative features also supported iterative refinement.

  * ###  Accessibility embedded throughout
    The project consistently applied principles, including high contrast colours, readable typography, keyboard navigation and text back feedback.        These decisions align with UK Government Accessible guidelines and the EA's commitment to inclusive digital services:   https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps.
 
  * Testing was robust and balanced
  * CSV storage kept the system lightweight

 
### 6.2 What could be improved
Although the project met the MVP goals, several areas could be enhanced in future iterations.

  ### More advanced authentication
  The login is functional and basic.  A more secure approach  like hashed passwords would improve security and align with best practice guidance from the OWASP Authentication cheatsheet could inform future improvements.https://owasp.org/www-project-cheat-sheets/

  * More unit tests could be added
  * Additional question types could  enhance engagement
  * Enabling users to create their own username and password to access the system


### 6.3 Reflection
Building this project highlighted how even a small application benefits from clear architecture, testing, and documentation.  This dual interface reinforced the value of separating concerns, and focus on accessibility made the design more thoughtful and user-centred.  There is room for improvement.  The EA Hybrid Quiz system successfully delivers an accessible and training tool for staff, with both desktop interfaces, a modular architecture and documentation ready for deployment and future expansion.

