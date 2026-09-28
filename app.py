import os
import streamlit as st
from google import genai

# -----------------------------
# EduGenie - Gemini Learning Assistant
# -----------------------------

st.set_page_config(
    page_title="EduGenie - AI Learning Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 EduGenie")
st.subheader("Google Gemini Powered Learning Assistant")
st.write("Learn topics, ask questions, summarize notes, generate quizzes, and create study plans.")

# Read Gemini API key securely from an environment variable.
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("GEMINI_API_KEY is not set. Add your Gemini API key as an environment variable and restart the app.")
    st.stop()

client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.8-flash"

def ask_gemini(prompt):
    """Send a prompt to Gemini and return the generated answer."""
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("📚 Learning Tools")
tool = st.sidebar.selectbox(
    "Choose a tool",
    [
        "AI Tutor",
        "Explain a Topic",
        "Summarize Notes",
        "Generate Quiz",
        "Study Plan"
    ]
)

# -----------------------------
# AI Tutor
# -----------------------------
if tool == "AI Tutor":
    st.header("💬 AI Tutor")
    question = st.text_area(
        "Enter your question",
        placeholder="Example: Explain inheritance in Python with a simple example."
    )

    level = st.selectbox("Learning level", ["Beginner", "Intermediate", "Advanced"])

    if st.button("Ask EduGenie"):
        if question.strip():
            prompt = f"""
You are EduGenie, a friendly educational assistant.
Student level: {level}

Answer the student's question:
{question}

Rules:
- Explain clearly and accurately.
- Use simple language.
- Give examples when useful.
- Use headings and bullet points.
- Do not invent facts.
"""
            st.markdown(ask_gemini(prompt))
        else:
            st.warning("Please enter a question.")

# -----------------------------
# Explain Topic
# -----------------------------
elif tool == "Explain a Topic":
    st.header("📖 Explain a Topic")
    topic = st.text_input("Enter the topic", placeholder="Example: Object Oriented Programming")
    level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])

    if st.button("Explain Topic"):
        if topic.strip():
            prompt = f"""
Teach the topic "{topic}" to a {level} student.

Include:
1. Definition
2. Main concepts
3. Simple real-world example
4. Small programming example if relevant
5. Short summary
6. Three important points to remember
"""
            st.markdown(ask_gemini(prompt))
        else:
            st.warning("Please enter a topic.")

# -----------------------------
# Summarize Notes
# -----------------------------
elif tool == "Summarize Notes":
    st.header("📝 Summarize Notes")
    notes = st.text_area("Paste your notes here", height=250)

    if st.button("Create Summary"):
        if notes.strip():
            prompt = f"""
Summarize the following student notes.

Requirements:
- Keep the important ideas.
- Use headings and bullet points.
- Define difficult terms briefly.
- End with a 5-point quick revision section.

Notes:
{notes}
"""
            st.markdown(ask_gemini(prompt))
        else:
            st.warning("Please paste some notes.")

# -----------------------------
# Generate Quiz
# -----------------------------
elif tool == "Generate Quiz":
    st.header("🧠 Quiz Generator")
    topic = st.text_input("Quiz topic", placeholder="Example: Python basics")
    count = st.slider("Number of questions", 3, 10, 5)
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

    if st.button("Generate Quiz"):
        if topic.strip():
            prompt = f"""
Create a {difficulty} quiz for students about "{topic}".

Create exactly {count} multiple-choice questions.
For each question:
- Give 4 options: A, B, C, D.
- Give the correct answer.
- Give a one-sentence explanation.

Format each question clearly.
"""
            st.markdown(ask_gemini(prompt))
        else:
            st.warning("Please enter a quiz topic.")

# -----------------------------
# Study Plan
# -----------------------------
else:
    st.header("📅 Study Plan Generator")
    subject = st.text_input("Subject", placeholder="Example: Computer Science")
    topics = st.text_area(
        "Topics to study",
        placeholder="Example:\nPython\nDBMS\nComputer Networks\nData Structures"
    )
    days = st.slider("Number of study days", 1, 30, 7)
    hours = st.slider("Hours per day", 1, 8, 2)

    if st.button("Create Study Plan"):
        if subject.strip() and topics.strip():
            prompt = f"""
Create a practical {days}-day study plan for a student.

Subject: {subject}
Topics:
{topics}

Available study time: {hours} hours per day.

For each day include:
- Topics
- Study tasks
- Practice/revision
- A small self-test

Keep the plan realistic and easy to follow.
"""
            st.markdown(ask_gemini(prompt))
        else:
            st.warning("Please enter the subject and topics.")

st.divider()
st.caption("EduGenie uses the Google Gemini API to generate educational responses.")
