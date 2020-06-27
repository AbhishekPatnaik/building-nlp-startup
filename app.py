import streamlit as st
from spacy_streamlit import visualize_ner
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import fasttext
import spacy

__path__ = "/Users/abhishekpatnaik/Documents/text_classifier/emotion_detection/model_emotion.bin"
model = fasttext.load_model(__path__)

sentence_input = st.text_input("Enter your sentence(Press Enter to apply)")

         
prediction = model.predict(sentence_input)

prediction_text = str(prediction[0][0]).upper()


st.write('Label:-')
st.write(str(prediction_text))


prediction_score = prediction[1][0]
st.write('Confidence Score:-')
st.write('{:.2f}'.format(round(prediction_score,2)))

# Building NER on top of it

nlp = spacy.load("en_core_web_md")
doc = nlp(sentence_input)
visualize_ner(doc, labels=nlp.get_pipe("ner").labels)
        
