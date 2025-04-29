import streamlit as st
import joblib

# Load model
model = joblib.load('mental_health_model.pkl')

# Define intent-response mapping
responses = {
    "feeling_sad": "I'm sorry you're feeling that way. Want to talk about it?",
    "anxiety": "Anxiety can be tough. Try taking deep breaths or grounding exercises.",
    "happy": "That's wonderful to hear! What made you feel happy today?",
    "stress": "Stress is common. Want me to suggest some relaxation techniques?",
    "angry": "Let it out—what’s making you feel this way?",
    "lonely": "You're not alone. I'm here to talk. Do you want to share more?",
}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Mental Health Chatbot 💬")

# Display previous messages
for msg in st.session_state.messages:
    role, content = msg
    if role == "user":
        st.markdown(f"**You:** {content}")
    else:
        st.markdown(f"**Bot:** {content}")

# Input box
user_input = st.text_input("Type your message")

if user_input:
    st.session_state.messages.append(("user", user_input))
    intent = model.predict([user_input])[0]
    response = responses.get(intent, "I'm here to listen. Tell me more.")
    st.session_state.messages.append(("bot", response))
    st.experimental_rerun()
