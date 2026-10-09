
import streamlit as st
import ollama

st.set_page_config(
    page_title="BunBun AI",
    page_icon="🐰",
    layout="centered"
)

st.title("🐰 BunBun AI")
st.caption("Your personal RAG chatbot")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "knowledge" not in st.session_state:
    st.session_state.knowledge = ""

st.subheader("📚 Knowledge Base")

uploaded_file = st.file_uploader(
    "Upload a TXT knowledge-base file",
    type=["txt"]
)

if uploaded_file:
    st.session_state.knowledge = (
        uploaded_file.getvalue().decode("utf-8", errors="ignore")
    )
    st.success("Knowledge base loaded!")

st.divider()
st.subheader("💬 Chat with BunBun")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask BunBun something...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    context = st.session_state.knowledge[:12000]

    prompt = f"""
You are BunBun, a friendly AI assistant.

Answer the user's question using the knowledge-base context
when relevant. If the context does not contain the answer,
say that clearly. Do not invent facts.

KNOWLEDGE BASE:
{context if context else "No knowledge base uploaded yet."}

USER QUESTION:
{question}
"""

    with st.chat_message("assistant"):
        try:
            response = ollama.chat(
                model="llama3.2",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response["message"]["content"]
            st.markdown(answer)

            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        except Exception as error:
            st.error(
                "Could not connect to Ollama. "
                "Ollama must be running with llama3.2 installed. "
                f"Details: {error}"
            )

if st.button("🗑️ Clear chat"):
    st.session_state.messages = []
    st.rerun()
