import streamlit as st
import random
from quiz_manager import QuizManager
from login_manager import LoginManager

qm = QuizManager()      # handles questions and answers
lm = LoginManager()     # handles login authentication

def main():
    # Track login state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Login screen
    if not st.session_state.logged_in:
        username = st.text_input("Username")                     # user enters name
        password = st.text_input("Password", type="password")    # hidden password field

        if st.button("Login") and lm.authenticate(username, password):
            st.session_state.logged_in = True                    # mark user as logged in
            st.experimental_rerun()                              # reload quiz screen
        return

    st.title("EA Hybrid Quiz")

    # Initialise score and question counter
    if "score" not in st.session_state:
        st.session_state.score = 0                               # number of correct answers
        st.session_state.q_count = 0                             # how many questions asked

    # Create a shuffled list of 5 unique questions
    if "question_list" not in st.session_state:
        st.session_state.question_list = random.sample(qm.questions, 5)

    # End of quiz
    if st.session_state.q_count >= 5:
        st.success(f"Score: {st.session_state.score}/5")         # show final score

        # Play Again button resets everything
        if st.button("Play Again"):
            st.session_state.score = 0
            st.session_state.q_count = 0
            st.session_state.question_list = random.sample(qm.questions, 5)
            st.experimental_rerun()
        return

    # Get next question in the shuffled list
    q = st.session_state.question_list[st.session_state.q_count]

    # Display question and options
    choice = st.radio(q.text, q.options)                         # user selects an answer

    # Submit button checks answer
    if st.button("Submit"):
        if qm.check(choice, q.answer):                           # compare user answer
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect. Correct answer: {q.answer}")

        st.session_state.q_count += 1                            # move to next question
        st.experimental_rerun()                                  # refresh page

main()



       

      
