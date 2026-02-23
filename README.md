# EA Hybrid Quiz

#1  Introduction
The Environment Agency(EA) operates across a wide range of environmental, regulatory, and operational domains, including flood risk management, pollution response, permitting, environmental monitoring, and incident management.  Staff and delivery partners must maintain a consistent baseline knowledge to ensure safe, compliant, and effective operations.  This includes understanding EA policies, procedures, environmental principles, and technical concepts relevant to decision-making.  In such a multidisciplinary environment, accessible digital learning tools play an important role in supporting competence, onboarding, and continuous professional development.

The EA Hybrid Quiz is an interactive learning application designed to strengthen staff understanding of key EA Topics.  The tool provides a structured quiz experience that can be used for training, induction, toolbox talks, or self-directed e-learning.  The (MVP) minimum viable product includes a login system, category and difficulty selection, question presenting optional answer validation, and instant feedback.  The quiz content can cover EA Basics, Flooding, Pollution, Regulation, or mathematical knowledge relevant to EA roles.

A key feature of this project is the hybrid interface approach, offering two front-end options:
  TKinter: a desktop-style GUI suitable for local use on EA laptops.
  Strealit: a browser-based interface ideal for demonstrations, remote access, and rapid deployment.

Both interfaces read from the same CSV-based data store, ensuring consistency and ease of maintenance.  The project uses Python and object-oriented programming principles, with classes for questions, quiz management, and authentication.  The system includes exception handling, input validation, and testable logic, supported by automated unit tests.

For the EA, this MVP is relevant because it provides a low-cost, accessible, and easily maintainable tool that supports organisational competence. The Hybrid design also demonstrates modern development practices, version control, documentation, and continuous integration, aligning with professional software engineering standards.

##2  Design Section
### Figma-style GUI design
<img width="931" height="772" alt="image" src="https://github.com/user-attachments/assets/f11d80de-d61f-4363-982a-37f248ced35d" />

Figma is a collaborative interface-design tool used to create wireframes, mockups, and interactive prototypes.
Designers use it to plan screen layouts, colours, typography, and other user journeys before coding begins.
For the EA HYbrid Quiz, Figma was used to sketch each screen i.e. (_Login_, _Welcome_, _Category Selection_, _Quiz_) ensure accessibility  and usability requirements are met in line with EA digital principles.

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
  +**Language:** Python 3
  +**GUI Frameworks:**
    +TKinter (desktop)
    +Streamlit (Web)
  
+**Data Storage:** CSV files (

+**Libraries:**
    +CSV - reading/writing data
    + TKinter - GUI
   + Streamlit - Web interface
   + unittest - automated testing
   + dataclasses - Question model
    
+**Tools:**
   + GitHub - version control
   + Figma -  interface prototyping
   + Streamlit - Web interface
   + VS Code - development environment
    
 ## Code design document   
  ### Class diagrams
<img width="642" height="705" alt="image" src="https://github.com/user-attachments/assets/989315fd-90de-4898-8edd-7567e2658afa" />

The UML  class diagrams provide a visual representation of the system's structure, showing classes, their attributes and methods, and the relationship between them. In the EA Hybrid Quiz, the class diagram clarifies how _LoginManager_, _QuizManager_, _Question_, _LoginWindow_, _TKQuizApp_, and the _Streamlit interface_ collaborate, supporting modularity, testability, and maintainability.


## Development Section
 
The EA Hybrid Quiz was developed using Python and follows a modular object-oriented structure.  The system is divided into logical components, data models, managers, and user interfaces to ensure maintainability, testability, and clarity.  This section explains the main modules and functions, showing how they work together to deliver the full quiz experience.

### Question (Question.py)
The _Question_ class represents a single question.  It stores the text, answer options, correct answer, difficulty, and category 

# Defines a simple Question object to store each quiz question
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

### QuizManager(quiz_manager.py)
_QuizManager_ handles loading questions from _CSV_ and checking answers.
It can be used and reused by TKinter and Streamlit.

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

++How it contributes
+ Loads data (FR2) from _CSV_
+ Converts raw CSV rows into _Question_
+ Provides a function (check) for unit testing
+ Ensure separation of concerns: logic stays out of GUI.


        

## Testing Section
### A third-level heading

## Documentation Section

## Evaluation Section

## A second-level heading

## A second-level heading


## A second-level heading



6 Evaluation



