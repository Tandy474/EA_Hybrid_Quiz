import unittest
from quiz_manager import QuizManager


# SMOKE TEST: ensures the QuizManager loads without crashing

class TestSmoke(unittest.TestCase):
    def test_quiz_manager_loads(self):
        qm = QuizManager()   # Should not raise any exceptions
        self.assertIsNotNone(qm.questions)  # Questions list should exist
        self.assertGreater(len(qm.questions), 0)  # Should load at least 1 question



# LOGIC TESTS: ensures answer checking works correctly

class TestQuizLogic(unittest.TestCase):
    def test_check_correct(self):
        qm = QuizManager()
        self.assertTrue(qm.check("A", "A"))  # Same answer → True

    def test_check_incorrect(self):
        qm = QuizManager()
        self.assertFalse(qm.check("B", "A"))  # Different answer → False



# RUN ALL TESTS

if __name__ == "__main__":
    unittest.main()
