import streamlit as st
import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Apple Inc. launched the iPhone 12 on October 23, 2020."

# Process the text
doc = nlp(text)

# Print named entities
for ent in doc.ents:
    st.write(ent.text, "→", ent.label_)