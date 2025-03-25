import streamlit as st
import time
import random

st.title("Quiz Application")

questions = [{
    "question": "What is the capital of Pakistan?",
    "options": ["Karachi", "Islamabad", "Lahore", "Peshawer"],
    "answer": "Islamabad"
},
{
    "question": "Which programming language is used for web development?",
    "options": ["Python", "Java", "JavaScript", "C++"],
    "answer": "JavaScript"
},
{
    "question": "What is the largest planet in our solar system?",
    "options": ["Earth", "Mars", "Jupiter", "Saturn"],
    "answer": "Jupiter"
},
{
    "question": "Who wrote the play 'Romeo and Juliet'?",
    "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
    "answer": "William Shakespeare"
},
{
    "question": "Which country is famous for the Eiffel Tower?",
    "options": ["Italy", "France", "Germany", "Spain"],
    "answer": "France"
},
{
    "question": "What is the chemical symbol for water?",
    "options": ["O2", "H2O", "CO2", "NaCl"],
    "answer": "H2O"
},
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

selected_option = st.radio("choose your answer", question["options"], key="answer")

if st.button("Submit answer"):
    if selected_option == question["answer"]:
        st.success("correct!")
        st.balloons()
    else:
        st.error("Incorrect! the correct answer is " + question["answer"])

    time.sleep(3)

    st.session_state.current_question = random.choice(questions)

    st.rerun()


