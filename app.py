import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("model/spam_classifier.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# App title
st.title("Spam Email Detector (TF-IDF + Naive Bayes)")

# Input box
user_input = st.text_area("Enter your email text below:", height=200)

# Predict button
if st.button("Detect"):
    if user_input.strip() == "":
        st.warning("Please enter some email text.")
    else:
        # Transform and predict
        transformed_input = vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)[0]
        
        label = "Spam" if prediction == 1 else "Ham"
        
        st.subheader("Prediction:")
        if label == "Spam":
            st.markdown(f"<h3 style='color:red;'> {label}</h3>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h3 style='color:green;'> {label}</h3>", unsafe_allow_html=True)

