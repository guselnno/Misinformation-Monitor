
import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Misinformation Monitor")

text = st.text_area("Klistra in en nyhetsartikel")

if st.button("Analysera"):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)

    if prediction[0] == 1:
        st.error("Artikeln liknar desinformation.")
    else:
        st.success("Artikeln liknar trovärdig information.")
