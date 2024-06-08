import streamlit as st
import cards
import time
import random

st.title('Tarot')
st.subheader('_Welcome to your digital Tarot Deck_', divider='blue')


# Buttons
blankcol, buttoncol = st.columns([1,1])

with blankcol:
    st.write("")
with buttoncol:
    but = st.button(":blue[Shuffle Deck]")

col1, col2, col3 = st.columns([2,2,1])

def run():
    random.shuffle(cards.images)
    time.sleep(0.5)
    with col2:
        st.image(cards.images[0], width = 250)
    time.sleep(0.5)

    with col1:
        st.image(cards.images[1], width = 250)
    time.sleep(0.5)

    with col3:
        st.image(cards.images[2], width = 250)

if but:
    run()
