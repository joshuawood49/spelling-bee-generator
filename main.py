import streamlit as st
import random

# Word data structure: word, pronunciation, definition, example
level_words = {
    "Level 1": [
        {
            "word": "above",
            "pronunciation": "uh-buv",
            "definition": "adverb: in a higher place.",
            "example": "Look above — there's a possum in the tree!"
        },
        {
            "word": "block",
            "pronunciation": "blok",
            "definition": "noun: a solid piece of hard material.",
            "example": "He built a tower out of wooden blocks."
        },
        # ⬅️ Add more Level 1 words here following this structure
    ],
    "Level 2": [
        {
            "word": "android",
            "pronunciation": "an-droid",
            "definition": "noun: a robot with a human appearance.",
            "example": "The android helped clean the space station."
        },
        # ⬅️ More Level 2 words...
    ],
    "Level 3": [],
    "Level 4": [],
    "Level 5": []
}

st.set_page_config(page_title="Spelling Bee Generator", layout="centered")
st.title("🐝 Spelling Bee Word Generator")
st.markdown("Pick a level to generate a random word. Each word includes pronunciation, definition, and a sentence. Words won’t repeat until you reset.")

selected_level = st.selectbox("Choose a spelling level:", list(level_words.keys()))

# Set up session state
if "used_words" not in st.session_state:
    st.session_state.used_words = {}
if selected_level not in st.session_state.used_words:
    st.session_state.used_words[selected_level] = []

col1, col2 = st.columns(2)

with col1:
    if st.button("🎲 Generate Word"):
        unused_words = [
            word for word in level_words[selected_level]
            if word["word"] not in [w["word"] for w in st.session_state.used_words[selected_level]]
        ]
        if unused_words:
            new_word = random.choice(unused_words)
            st.session_state.used_words[selected_level].append(new_word)
            st.markdown(f"### 📝 {new_word['word']}")
            st.markdown(f"**Pronunciation:** {new_word['pronunciation']}")
            st.markdown(f"**Definition:** {new_word['definition']}")
            st.markdown(f"**Example:** {new_word['example']}")
        else:
            st.warning("✅ All words shown for this level. Please reset to start again.")

with col2:
    if st.button("🔁 Reset Words"):
        st.session_state.used_words[selected_level] = []
        st.info(f"{selected_level} word list has been reset.")
