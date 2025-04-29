import streamlit as st
import joblib

model = joblib.load('mental_health_model.pkl')

st.title("Mental Health Chatbot 💬")
st.write("Hi, I’m here to help. Tell me how you’re feeling.")

user_input = st.text_input("You:")

if user_input:
    prediction = model.predict([user_input])[0]
    
    # Add your own mapped responses here
    responses = {
        "feeling_sad": "I'm sorry you're feeling that way. Want to talk about it?",
        "anxiety": "Anxiety can be tough. Try taking deep breaths or grounding exercises.",
        "happy": "That's wonderful to hear! What made you feel happy today?",
        "stress": "Stress is common. Want me to suggest some relaxation techniques?",
        "angry": "Let it out—what’s making you feel this way?",
        "lonely": "You're not alone. I'm here to talk. Do you want to share more?",
        # Add more intent-response pairs here
    }
    
    response = responses.get(prediction, "I'm here to listen. Tell me more.")
    st.text_area("Bot:", value=response, height=100)
