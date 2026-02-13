import streamlit as st
from groq import Groq

client = Groq(api_key="api")

data = [
    "Python is a programming language.",
    "Java is used for application development.",
    "AI means Artificial Intelligence.",
    "Machine learning is a part of AI."
]

def get_context(question):
    question = question.lower()
    for line in data:
        for word in question.split():
            if word in line.lower():
                return line
    return None

def chatbot(question):
    context = get_context(question)
    if not context:
        return "I don't know the answer."

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Answer only using the given context."},
            {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

st.set_page_config(page_title="General Q/A Chatbot", layout="centered")

st.title("General Q/A Chatbot")
st.write("Ask questions based on stored knowledge")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        answer = chatbot(question)
        st.success(answer)

st.markdown("---")
st.caption("Simple RAG-based Q/A Chatbot using Streamlit")



