import streamlit as st
import time

st.title('Tarot')
st.subheader('_Welcome to your digital Tarot Deck_', divider='blue')

# Buttons
blankcol, buttoncol = st.columns([1,1])

with blankcol:
    st.write("")
with buttoncol:
    st.button(":blue[Shuffle Deck]")


# Cards
images = ["assets/Fool.jpeg",
          "assets/HighPriestess.jpeg",
          "assets/World.jpeg"]

col1, col2, col3 = st.columns([2,2,1])

with col1:
    st.image(images[1], width = 250)

with col2:
    st.image(images[0], width = 250)

with col3:
    st.image(images[2], width = 250)

for i in images:
    with col2:
        a = st.image(i, width = 250)
    time.sleep(1)
    a.empty()