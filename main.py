import streamlit as st
import cards
import variables
import time
import random

st.title('Tarot')
st.header('_Welcome to your digital Tarot Deck_', divider='blue')

blankcol, writecol = st.columns([1.2,2])
with blankcol:
    st.write("")
with writecol:
    st.write("Display three cards for today")

# Shuffle Button
blankcol, buttoncol = st.columns([1.5,2])
with blankcol:
    st.write("")
with buttoncol:
    shufbutton = st.button(":blue[Shuffle Deck]")

def shuffle():
    """
    Returns three random cards
    """
    col1, col2, col3 = st.columns([2,2,1])
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

if shufbutton:
    shuffle()

# Celtic Cross Spread
blankcol, subheadcol = st.columns([1.4,2])
with blankcol:
    st.write("")
with subheadcol:
    st.subheader(':blue[Celtic Cross]')

st.write("The Celtic cross tarot spread is the oldest and most-classic of all the tarot spreads. The first published reference to it was by Arthur Edward Waite, the co-creator of the popular Rider Waite Tarot Deck")
st.write("The Celtic cross tarot spread consists of 10 card positions representing different questions, and together they form the shape of a cross, with a vertical row of four cards laid out to its right. ")
def celtic():
    """
    Displays ten cards for the Celtic Cross
    """
    random.shuffle(variables.cards["Major Arcana"])
    random.shuffle(variables.cards["The Wands"])
    random.shuffle(variables.cards["The Cups"])
    random.shuffle(variables.cards["The Swords"])
    random.shuffle(variables.cards["The Pentacles"])

    rep = ["_Card 1_ : The querent → ", "_Card 2_ : The block → ", "_Card 3_ : The root → ", "Card 4: The recent past → ",
           "_Card 5_ : Possibilities → ", "_Card 6_ : Where you’re headed → ", "_Cards 7_ : How you view yourself right now → ",
           "_Card 8_ : Your environment → ", "_Card 9_ : Hopes and fears → ", "_Card 10_ : The outcome → "]
    celtic = []

    for i in range(2):
        celtic.append(variables.cards["Major Arcana"][i])
        celtic.append(variables.cards["The Wands"][i])
        celtic.append(variables.cards["The Cups"][i])
        celtic.append(variables.cards["The Swords"][i])
        celtic.append(variables.cards["The Pentacles"][i])

    for i,val in zip(rep,celtic):
        st.write(i,val)

# Celtic Button
blankcol, buttoncol = st.columns([1.5,2])
with blankcol:
    st.write("")
with buttoncol:
    celtbutton = st.button(":blue[Celtic Cross]")

if celtbutton:
    celtic()