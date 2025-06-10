import streamlit as st
import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Apple Inc. unveiled the iPhone 12 at an event in Cupertino on October 13, 2020."

# Process the text
doc = nlp(text)

# Print named entities
for ent in doc.ents:
    st.write(ent.text, "→", ent.label_)
