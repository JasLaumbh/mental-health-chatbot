import streamlit as st

# Set page config at the very top
st.set_page_config(page_title="Mental Health Chatbot", layout="centered")

# Title and logo
st.markdown("<h1 style='text-align: center;'>🧠 Mental Health Chatbot</h1>", unsafe_allow_html=True)

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Hi there! I'm here to support you. How are you feeling today?"}
    ]

# Function to detect emotion based on user input
def detect_emotion(user_input):
    text = user_input.lower()

    if any(word in text for word in ["angry", "furious", "mad", "annoyed"]):
        return "anger"
    elif any(word in text for word in ["sad", "down", "depressed", "unhappy", "cry","not good"]):
        return "sadness"
    elif any(word in text for word in ["anxious", "nervous", "worried", "stressed"]):
        return "anxiety"
    elif any(word in text for word in ["happy", "joyful", "good", "great", "fine","not sad"]):
        return "happiness"
    elif any(word in text for word in ["lonely", "alone", "isolated"]):
        return "loneliness"
    else:
        return "neutral"

# Function to generate a bot response based on detected emotion
def generate_bot_response(emotion):
    responses = {
        "anger": "It's okay to feel angry sometimes. Would you like to talk about what's upsetting you?",
        "sadness": "I'm really sorry you're feeling this way. You're not alone—I'm here for you.",
        "anxiety": "Anxiety can feel overwhelming. Let's take a deep breath together. What's on your mind?",
        "happiness": "That's wonderful! I'm happy you're feeling good. What made your day better?",
        "loneliness": "Loneliness can be tough. I'm here to listen. Want to tell me more about how you're feeling?",
        "neutral": "Thanks for sharing. Want to talk more about your day or anything on your mind?"
    }
    return responses.get(emotion, responses["neutral"])

# Display conversation history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['text']}")
    else:
        st.markdown(f"**Bot:** {message['text']}")

# Input form for user message
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", "")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "text": user_input})

    # Detect emotion based on user input
    emotion = detect_emotion(user_input)

    # Generate a bot reply based on detected emotion
    bot_response = generate_bot_response(emotion)

    # Append bot reply
    st.session_state.messages.append({"role": "bot", "text": bot_response})

