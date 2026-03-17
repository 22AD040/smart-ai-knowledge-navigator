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
background: linear-gradient(135deg,#eef2ff,#fdf2f8);
}

/* Title gradient */

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
opacity:0.8;
margin-bottom:20px;
}

/* result card */

.result-card{
padding:20px;
border-radius:12px;
border:1px solid rgba(0,0,0,0.1);
background: var(--secondary-background-color);
margin-bottom:18px;
}

/* chat bubbles */

.chat-user{
padding:12px;
border-radius:10px;
background: rgba(99,102,241,0.15);
margin-bottom:8px;
}

.chat-ai{
padding:12px;
border-radius:10px;
background: rgba(236,72,153,0.15);
margin-bottom:12px;
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
### How this page works

Upload a dataset or document and the system will:

1️⃣ Extract text from the file  
2️⃣ Convert the text into **vector embeddings**  
3️⃣ Store vectors inside **FAISS vector database**

This enables **semantic search instead of keyword search**.

### Example

Input:
Upload `dataset.csv`

Output:
Document indexed successfully
""")

    file = st.file_uploader("Upload PDF / TXT / CSV")

    if file:

        text = extract_text(file)

        add_document(text)

        st.success("✅ Document indexed successfully!")





if menu == "Semantic Search":

    st.header("🔎 Semantic Search Engine")

    st.info("""
### How this page works

Semantic search finds **meaning**, not just keywords.

Process:

1️⃣ Convert query into embedding  
2️⃣ Compare with FAISS vector database  
3️⃣ Calculate cosine similarity  
4️⃣ Return most relevant documents

Example query:

`What affects employee attrition?`
""")

    query = st.text_input("Ask a question")

    if query:

        results = search(query)

        if len(results) == 0:

            st.warning("⚠ Upload documents first.")

        else:

            st.subheader("Top Results")

            for i, r in enumerate(results):

                st.markdown(f"""
<div class="result-card">

### Result {i+1}

**Similarity Score:** `{r['score']}`

**Snippet**

{r['text']}...

</div>
""", unsafe_allow_html=True)





if menu == "Similarity Analyzer":

    st.header("🧠 Sentence Similarity Analyzer")

    st.info("""
### How this page works

This tool measures **semantic similarity between two sentences**.

The system:

1️⃣ Converts both sentences into embeddings  
2️⃣ Uses cosine similarity  
3️⃣ Returns similarity score

Example:

Sentence 1:
AI improves healthcare

Sentence 2:
Machine learning helps hospitals
""")

    s1 = st.text_area("Sentence 1")

    s2 = st.text_area("Sentence 2")

    if st.button("Analyze Similarity"):

        score = similarity(s1, s2)

        st.metric("Similarity Score", round(score,3))





if menu == "Weather AI":

    st.header("🌦 Weather Intelligence")

    st.info("""
### How this page works

This module uses **Weather API + AI insight generation**

Process:

1️⃣ User enters city  
2️⃣ Weather API fetches data  
3️⃣ AI summarizes insights

Example:

City: Chennai
""")

    city = st.text_input("Enter City")

    if city:

        result = weather_insight(city)

        st.success(result)





if menu == "AI Chatbot":

    st.header("🤖 AI Assistant")

    st.info("""
### How this page works

This chatbot uses **Gemini 2.5 Flash LLM**.

Features:

• remembers previous conversation  
• generates intelligent answers  
• contextual responses
""")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

   
    for chat in st.session_state.chat_history:

        if chat["role"] == "user":
            st.markdown(f'<div class="chat-user">👤 {chat["content"]}</div>', unsafe_allow_html=True)

        else:
            st.markdown(f'<div class="chat-ai">🤖 {chat["content"]}</div>', unsafe_allow_html=True)

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