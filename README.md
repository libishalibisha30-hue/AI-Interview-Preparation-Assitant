# AI Interview Preparation Assistant Using LLM

## 1. Project Overview

The AI Interview Preparation Assistant is a web-based application developed using Python, Streamlit, and Google's Gemini API.

This application uses an existing pre-trained Large Language Model (LLM), Google Gemini, to understand user queries and generate relevant interview-related responses.

Instead of developing or training a language model from scratch, this project integrates the existing Gemini model through its API. It provides an interactive platform where users can ask interview-related questions and receive AI-generated answers.

## 2. Objectives

- To develop an AI-powered interview preparation assistant.
- To integrate an existing pre-trained Large Language Model into a web application.
- To provide instant responses to interview-related questions.
- To help students improve their interview preparation.
- To demonstrate the practical application of Generative AI and LLMs.

## 3. Features

- **Ask AI:** Users can ask interview-related questions.
- **AI-Generated Responses:** Generates relevant answers using Google's Gemini model.
- **Chat History:** Maintains previous conversations.
- **Interactive Interface:** Provides a user-friendly interface using Streamlit.
- **Conversation Access:** Users can revisit previous questions and responses through the sidebar.

## 4. Technologies Used

- **Python:** Used for application development and backend logic.
- **Streamlit:** Used to create the interactive web interface.
- **Google Gemini API:** Used to communicate with the existing pre-trained LLM.
- **Large Language Model (LLM):** Google Gemini is used to understand user input and generate responses.
- **Python Libraries:** Used for API integration and application functionality.

## 5. Project Structure

```text
AI_Interview_Assitant/
│
├── app.py
├── test_gemini.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

**Note:** The `.env` file stores the Gemini API key and must not be uploaded to GitHub. The `.gitignore` file prevents sensitive information from being pushed to the repository.

## 6. Installation and Execution

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd AI_Interview_Assitant
```

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 4: Configure Gemini API

Create a `.env` file in the project folder and add your Gemini API key.

```env
GEMINI_API_KEY=your_api_key
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open in your web browser.

## 7. Working Principle

1. The user opens the AI Interview Preparation Assistant.
2. The user enters an interview-related question in the Ask AI section.
3. The Python application receives the user's input.
4. The application sends the question to Google's Gemini API.
5. The existing pre-trained Gemini LLM processes the input and generates a response.
6. The generated answer is displayed on the Streamlit interface.
7. Previous conversations can be accessed through the chat history in the sidebar.

## 8. Role of the Pre-trained LLM

This project uses Google's Gemini, an existing pre-trained Large Language Model.

A pre-trained LLM is a language model that has already been trained on large amounts of data to understand and generate human-like text.

In this application:

- The Gemini model is not created or trained by the developer.
- The existing model is accessed through the Gemini API.
- User questions are provided as prompts to the model.
- The model generates responses based on the given input.
- Python integrates the model into the Streamlit application.

## 9. Applications

- Technical interview preparation.
- General interview question practice.
- Understanding technical concepts.
- Learning through AI-generated explanations.
- Improving interview readiness.

## 10. Conclusion

The AI Interview Preparation Assistant demonstrates the practical integration of an existing pre-trained Large Language Model into a web-based application.

By using Google's Gemini API with Python and Streamlit, the project provides an interactive platform for interview preparation. It highlights how existing Generative AI models can be integrated into real-world applications without developing or training a language model from scratch.