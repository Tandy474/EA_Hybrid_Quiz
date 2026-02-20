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

