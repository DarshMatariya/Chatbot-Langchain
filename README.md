# LangChain Chatbot

A conversational chatbot powered by [LangChain](https://python.langchain.com/) and OpenAI's large language models. This project is designed for developers exploring GenAI tools and building interactive, intelligent applications.

---

## Features

- LangChain + Gemini integration
- Secure API key loading via `.env`
- Human-like responses with LLMs
- CLI-based interface using Streamlit

---

## Project Structure
Langchain-Chatbot/
- chatbot.py # Main script to run chatbot
- .env.example # Sample env variables file
- requirements.txt # Python dependencies
- README.md # Project info and usage


---

## Installation

### How to run ?

1. Clone the repository:  
   git clone https://github.com/DarshMatariya/Chatbot-Langchain.git

2. Create virtual environment
  python -m venv venv
  source venv/bin/activate    # on Linux/macOS
  venv\Scripts\activate       # on Windows

3. Install Requirements
  pip install -r requirements.txt

4. API Key Setup
   GOOGLE_API_KEY=your-api-key-here

5.Run chatbot.py file
  streamlit run chatbot.py

## Tech Stack

Python 3.10+
LangChain
Gemin API
dotenv for secrets management


Feel free to open issues or submit pull requests for improvements.





