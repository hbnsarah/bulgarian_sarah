import streamlit as st
import pandas as pd
import random

st.title("Bulgarian Trainer for Sarah")

words = pd.read_csv(
    "words_bulgarian_english.csv",
    header=None,
    names=["bulgarian", "english", "category"],
    skiprows=1,
    sep=";",
    encoding="utf-8-sig",
    encoding_errors="replace"
)

if "current_word" not in st.session_state:
    st.session_state.current_word = words.sample(1).iloc[0]

if "answer" not in st.session_state:
    st.session_state.answer = ""

def next_word():
    st.session_state.current_word = words.sample(1).iloc[0]
    st.session_state.answer = ""

word = st.session_state.current_word

st.subheader("Translate this word:")
st.write(f"### {word['bulgarian']}")

answer = st.text_input(
    "Your answer:",
    key="answer"
)

if st.button("Check"):
    correct_answer = str(word["english"]).lower().strip()
    user_answer = st.session_state.answer.lower().strip()

    if user_answer == correct_answer:
        st.success("Correct!")
    else:
        st.error(f"It's not correct Noob!. The correct answer is: {word['english']}")

st.button("Next word", on_click=next_word)