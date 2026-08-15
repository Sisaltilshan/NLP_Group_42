import streamlit as st
import pandas as pd
import re
import joblib  # or import torch/transformers if using saved deep learning models

# Set page configuration
st.set_page_config(page_title="Intelligent Email Spam Detector", layout="wide")

# App Header
st.title("📧 Intelligent Email Spam Detection System")
st.markdown("Enter email content below to analyze whether it is **Spam** or **Ham**, get a summary breakdown, and receive safety guidance.")

# Load Champion Model artifacts
@st.cache_resource
def load_model():
    # Replace with path to your saved model file in models/
    # Example: return joblib.load('models/xgboost_spam_model.pkl')
    pass

# Helper text cleaner
def clean_text(t):
    t = str(t).lower()
    t = re.sub(r'<.*?>', '', t)
    t = re.sub(r'http\S+', '', t)
    t = re.sub(r'[^a-z\s]', '', t)
    return re.sub(r'\s+', ' ', t).strip()

# Main Interface Layout
col1, col2 = st.columns([2, 1])

with col1:
    email_input = st.text_area("Paste Raw Email Content Here:", height=200)
    analyze_btn = st.button("Analyze Email")

    if analyze_btn and email_input.strip():
        cleaned = clean_text(email_input)
        
        # Calculate key linguistic features (from your XGBoost pipeline)
        length = len(cleaned)
        exclaims = email_input.count('!')
        caps_ratio = sum(1 for c in email_input if c.isupper()) / (len(email_input) + 1)
        
        # Simple heuristic mockup / model invocation
        is_spam = exclaims > 2 or caps_ratio > 0.2 or "free" in cleaned or "click" in cleaned
        confidence = 0.92 if is_spam else 0.95
        
        st.subheader("Analysis Results")
        if is_spam:
            st.error(f"⚠️ **SPAM / PHISHING DETECTED** (Confidence: {confidence * 100:.1f}%)")
        else:
            st.success(f"✅ **LEGITIMATE EMAIL (HAM)** (Confidence: {confidence * 100:.1f}%)")
            
        st.markdown("---")
        st.subheader("🔍 Risk Breakdown & Summary")
        st.write(f"- **Text Length:** {length} characters")
        st.write(f"- **Exclamation Marks:** {exclaims}")
        st.write(f"- **Capitalization Ratio:** {caps_ratio * 100:.1f}%")
        if is_spam:
            st.warning("Flagged due to high concentration of urgent punctuation, capital letters, or suspicious keyword patterns.")

# Sidebar Chatbot for Security Advisory
with col2:
    st.sidebar.title("🤖 Security Assistant")
    st.sidebar.info("Ask the AI advice on suspicious links or email safety best practices.")
    user_query = st.sidebar.text_input("Ask advice:")
    if user_query:
        st.sidebar.write("💡 **Safety Tip:** Never click unsolicited links or download unexpected attachments from unverified senders.")
