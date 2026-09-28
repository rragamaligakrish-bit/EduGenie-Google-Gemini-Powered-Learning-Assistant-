# EduGenie - Google Gemini Powered Learning Assistant

EduGenie is a student-focused AI learning assistant built with Python, Streamlit, and the Google Gemini API.

## Features

- AI Tutor
- Explain a Topic
- Summarize Notes
- Generate Multiple-Choice Quizzes
- Create Study Plans

## Project Structure

```text
EduGenie/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

1. Install Python.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a Gemini API key in Google AI Studio.
4. Set the API key as an environment variable named `GEMINI_API_KEY`.
5. Run:

```bash
streamlit run app.py
```

## Security

Do not put your Gemini API key directly in `app.py` or upload it to GitHub.
