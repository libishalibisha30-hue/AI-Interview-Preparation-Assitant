import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Page configuration
st.set_page_config(
    page_title="AI Interview Assistant",
    layout="wide"
)

# Title
st.title("AI Interview Preparation Assistant")

st.write(
    "Practice interview questions with an AI interviewer "
    "and receive instant feedback."
)


   # Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar
st.sidebar.title("☰ Menu")

show_history = st.sidebar.checkbox(" Chat History")


# Main page
st.subheader(" Ask the AI")

user_prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Example: Explain SQL joins in simple English with an example.",
    height=150
)

if st.button(" Ask AI"):

    if user_prompt.strip() == "":
        st.warning("Please enter a prompt first.")

    else:
        with st.spinner("AI is thinking..."):

            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=user_prompt
                )

                # Store question and answer
                st.session_state.chat_history.append(
                    {
                        "question": user_prompt,
                        "answer": response.text
                    }
                )

                # Display current answer
                st.subheader(" AI Response")
                st.write(response.text)

            except Exception:
                st.error(
                    "The AI service is temporarily unavailable. "
                    "Please wait a few seconds and try again."
                )


# Show chat history only when selected
if show_history:

    st.sidebar.markdown("---")
    st.sidebar.subheader(" Chat History")

    if len(st.session_state.chat_history) == 0:

        st.sidebar.info("No chat history yet.")

    else:

        for i, chat in enumerate(
            reversed(st.session_state.chat_history)
        ):

            question_number = len(st.session_state.chat_history) - i

            if st.sidebar.button(
                f"{question_number}. {chat['question'][:45]}...",
                key=f"history_{i}"
            ):

                st.session_state.selected_chat = chat


# Display selected history
if "selected_chat" in st.session_state:

    st.markdown("---")
    st.subheader(" Selected Conversation")

    st.markdown("** Your Question:**")
    st.info(st.session_state.selected_chat["question"])

    st.markdown("** AI Response:**")
    st.write(st.session_state.selected_chat["answer"])