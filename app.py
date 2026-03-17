import streamlit as st
from modules.semantic_search import add_document, search
from modules.document_processor import extract_text
from modules.similarity_checker import similarity
from modules.chatbot import ask_ai
from modules.weather_ai import weather_insight


st.set_page_config(
    page_title="Smart AI Knowledge Navigator",
    page_icon="🧠",
    layout="wide"
)




st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
var(--background-color),
var(--secondary-background-color)
);
}

/* Title */

.main-title{
font-size:40px;
font-weight:700;
background: linear-gradient(90deg,#6366f1,#ec4899);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

/* subtitle */

.subtitle{
font-size:16px;
color: var(--text-color);
opacity:0.8;
margin-bottom:20px;
}

/* cards */

.result-card{
padding:20px;
border-radius:12px;
border:1px solid rgba(0,0,0,0.08);
background: var(--background-color);
color: var(--text-color);
box-shadow:0 4px 12px rgba(0,0,0,0.06);
margin-bottom:18px;
}

/* user chat */

.chat-user{
padding:14px;
border-radius:10px;
background: rgba(99,102,241,0.15);
color: var(--text-color);
margin-bottom:10px;
}

/* ai chat */

.chat-ai{
padding:14px;
border-radius:10px;
background: rgba(236,72,153,0.15);
color: var(--text-color);
margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)




st.markdown('<div class="main-title">🧠 Smart AI Knowledge Navigator</div>', unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">AI powered semantic search and knowledge intelligence platform</div>',
unsafe_allow_html=True
)




menu = st.sidebar.selectbox(
"Navigation",
[
"Upload Document",
"Semantic Search",
"Similarity Analyzer",
"Weather AI",
"AI Chatbot"
]
)




if menu == "Upload Document":

    st.header("📄 Upload Knowledge Document")

    st.info("""
Upload a document or dataset.

Process:

1️⃣ Extract text from file  
2️⃣ Convert text to embeddings  
3️⃣ Store embeddings in FAISS vector database

Example: Upload `dataset.csv`
""")

    file = st.file_uploader("Upload PDF / TXT / CSV")

    if file:

        text = extract_text(file)

        add_document(text)

        st.success("Document indexed successfully!")





if menu == "Semantic Search":

    st.header("🔎 Semantic Search Engine")

    st.info("""
Semantic search finds **meaning**, not keywords.

Example query:

`What affects employee attrition?`
""")

    query = st.text_input("Ask a question")

    if query:

        results = search(query)

        if len(results) == 0:

            st.warning("Upload documents first.")

        else:

            st.subheader("Top Results")

            for i, r in enumerate(results):

                st.markdown(f"""
<div class="result-card">

### Result {i+1}

Similarity Score: **{r['score']}**

Snippet:

{r['text']}...

</div>
""", unsafe_allow_html=True)





if menu == "Similarity Analyzer":

    st.header("🧠 Sentence Similarity Analyzer")

    st.info("""
Compare semantic similarity between two sentences.
""")

    s1 = st.text_area("Sentence 1")

    s2 = st.text_area("Sentence 2")

    if st.button("Analyze Similarity"):

        score = similarity(s1, s2)

        st.metric("Similarity Score", round(score,3))





if menu == "Weather AI":

    st.header("🌦 Weather Intelligence")

    st.info("""
Enter a city to fetch weather insights using API.
""")

    city = st.text_input("Enter City")

    if city:

        result = weather_insight(city)

        st.success(result)





if menu == "AI Chatbot":

    st.header("🤖 AI Assistant")

    st.info("""
Chatbot powered by **Gemini 2.5 Flash**.

It remembers previous conversation.
""")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for chat in st.session_state.chat_history:

        if chat["role"] == "user":

            st.markdown(
            f'<div class="chat-user">👤 {chat["content"]}</div>',
            unsafe_allow_html=True
            )

        else:

            st.markdown(
            f'<div class="chat-ai">🤖 {chat["content"]}</div>',
            unsafe_allow_html=True
            )

    prompt = st.chat_input("Ask AI anything")

    if prompt:

        st.session_state.chat_history.append({
        "role":"user",
        "content":prompt
        })

        response = ask_ai(prompt)

        st.session_state.chat_history.append({
        "role":"assistant",
        "content":response
        })

        st.rerun()