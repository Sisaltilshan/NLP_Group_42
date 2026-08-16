"""
Group 42 - Intelligent Email Spam Detection - Final Application
Best model: SVM (F1 Score = 0.94 in our Colab evaluation)

WHY THIS VERSION IS DIFFERENT: loading a model trained in Colab caused a
scikit-learn version-mismatch error on this computer. This version trains
the SVM fresh, directly here, using this computer's own scikit-learn --
so there's no version conflict. Training only takes a few seconds since
the dataset is small.

HOW TO RUN:
1. Put this file inside a folder, e.g. Desktop/SpamApp/app.py
2. Put spam_dataset.csv in that SAME folder (not inside models/)
3. Command Prompt: cd Desktop\\SpamApp
4. pip install streamlit scikit-learn pandas
5. python -m streamlit run app.py
"""

import streamlit as st
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

st.set_page_config(page_title="Email Spam Detector", page_icon="📧")

def clean_text(t):
    t = str(t).lower()
    t = re.sub(r'<.*?>', ' ', t)
    t = re.sub(r'http\S+', ' ', t)
    t = re.sub(r'[^a-z\s]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()

# @st.cache_resource means this training only happens ONCE, the first time
# the app runs -- after that it's instant, Streamlit remembers it.
@st.cache_resource
def train_model():
    df = pd.read_csv("spam_dataset.csv")
    df['clean'] = df['text'].apply(clean_text)

    vectorizer = TfidfVectorizer(max_features=3000)
    X = vectorizer.fit_transform(df['clean'])
    y = df['label']

    model = SVC(kernel='linear')
    model.fit(X, y)

    return model, vectorizer

with st.spinner("Training model, please wait a moment..."):
    model, vectorizer = train_model()

def predict(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]
    is_spam = (prediction == 'spam') or (prediction == 1)
    return is_spam


st.title("📧 Intelligent Email Spam Detection")
st.write("Paste an email below and the system will classify it as **Spam** or **Ham** (legitimate).")
st.caption("Powered by an SVM model — the best performer in our evaluation (F1 Score: 0.94)")

email_text = st.text_area("Email content", height=200, placeholder="Paste the email text here...")

if st.button("Analyze"):
    if not email_text.strip():
        st.warning("Please paste some email text first.")
    else:
        is_spam = predict(email_text)
        if is_spam:
            st.error("🚨 **SPAM DETECTED**")
        else:
            st.success("✅ **Legitimate email (Ham)**")

st.markdown("---")
st.caption("Group 42 — CCS3356 Natural Language Processing — Intelligent Email Spam Detection Using ML and DL Approaches")
