# 🧠 Smart AI Knowledge Navigator

An **AI-powered semantic search and knowledge intelligence platform** built using **Streamlit, FAISS, Gemini 2.5 Flash, and Machine Learning**.

The application allows users to **upload documents, perform semantic search, analyze text similarity, access weather intelligence, and interact with an AI assistant** — all within a modern interactive interface.

---

# 🚀 Project Overview

Traditional search engines rely on **keyword matching**, which often fails to capture the true meaning of a query.

**Smart AI Knowledge Navigator** solves this by using:

* **Vector embeddings**
* **FAISS vector database**
* **Semantic similarity search**
* **Large Language Models (Gemini AI)**

This enables the system to **understand context and meaning**, delivering **more accurate and intelligent results**.

---

# 🏗 System Architecture

```
User Input
    ↓
Text Embedding
    ↓
Vector Database (FAISS)
    ↓
Similarity Search
    ↓
Top Relevant Results
    ↓
Streamlit UI
```

For AI responses:

```
User Query
   ↓
Gemini 2.5 Flash
   ↓
Context + Conversation Memory
   ↓
AI Generated Response
```

---

# ✨ Features

### 🔎 Semantic Search Engine

Search documents based on **meaning instead of keywords**.

Example:

Input

```
What affects employee attrition?
```

Output

```
Relevant document snippets discussing employee satisfaction,
workload, company policies, and turnover trends.
```

---

### 📄 Document Knowledge Base

Upload documents and convert them into **vector embeddings**.

Supported formats:

* PDF
* TXT
* CSV

The documents are stored in a **FAISS vector database** for fast semantic retrieval.

---

### 🧠 Sentence Similarity Analyzer

Measure how similar two sentences are using **cosine similarity on embeddings**.

Example:

Input

```
Sentence 1: AI helps doctors diagnose diseases
Sentence 2: Machine learning assists hospitals
```

Output

```
Similarity Score: 0.84
```

---

### 🌦 Weather Intelligence Module

Fetch real-time weather data using a **Weather API** and provide AI-generated insights.

Example:

Input

```
City: Chennai
```

Output

```
Temperature: 32°C
Humidity: 78%
Condition: Cloudy

AI Insight:
Carry an umbrella. Rain is likely today.
```

---

### 🤖 AI Chat Assistant

An intelligent chatbot powered by **Gemini 2.5 Flash**.

Capabilities:

* Context-aware responses
* Remembers previous conversation
* Generates detailed explanations

Example:

Input

```
Explain machine learning
```

Output

```
Machine learning is a field of artificial intelligence that enables
computers to learn patterns from data and improve predictions
without being explicitly programmed.
```

---

# 🎨 User Interface

The application features a **modern UI with gradients and card layouts** built using Streamlit.

Pages included:

| Page                | Description                              |
| ------------------- | ---------------------------------------- |
| Upload Document     | Upload and index documents               |
| Semantic Search     | Find information using vector similarity |
| Similarity Analyzer | Compare two sentences                    |
| Weather AI          | Get weather insights using API           |
| AI Chatbot          | Ask questions using Gemini AI            |

---

# 🧰 Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI / GenAI

* Gemini 2.5 Flash

### Vector Database

* FAISS

### Machine Learning

* Sentence Transformers
* Scikit-learn

### APIs

* Weather API

### Data Processing

* NumPy
* Pandas
* PyPDF2

---

# 📂 Project Structure

```
smart-ai-knowledge-navigator
│
├── app.py
│
├── modules
│   ├── semantic_search.py
│   ├── chatbot.py
│   ├── weather_ai.py
│   ├── similarity_checker.py
│   └── document_processor.py
│
├── utils
│   ├── embedding_utils.py
│   ├── api_utils.py
│   └── db_utils.py
│
├── vector_db
│   └── faiss_index
│
├── database
│   └── users.db
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/22AD040/smart-ai-knowledge-navigator.git
```

```
cd smart-ai-knowledge-navigator
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create `.env` file

```
GEMINI_API_KEY=your_gemini_api_key
WEATHER_API_KEY=your_weather_api_key
```

⚠ Do **not push `.env` to GitHub**

---

### 5️⃣ Run the Application

```
streamlit run app.py
```

Open in browser

```
http://localhost:8501
```

---

# ☁ Deployment (Streamlit Cloud)

1️⃣ Push project to GitHub

2️⃣ Go to

```
https://smart-ai-knowledge-navigator-wafw824rzwbftju3ph2gjc.streamlit.app/
```

3️⃣ Deploy repository

4️⃣ Add secrets

```
GEMINI_API_KEY
WEATHER_API_KEY
```

This prevents **API key leakage**.

---

# 🔐 Security Considerations

The project protects sensitive data by:

* Using `.env` for local secrets
* Using **Streamlit Secrets Manager** for deployment
* Ignoring `.env` and databases via `.gitignore`

---

# 📊 Example Use Case

Companies can use this system for:

* Internal knowledge search
* Document intelligence
* Research assistants
* AI powered knowledge bases

Example:

```
Employee asks:
How do we deploy ML models?

System retrieves:
Relevant documentation from company knowledge base
```

---

# 🌟 Future Improvements

Potential enhancements:

* Retrieval Augmented Generation (RAG)
* Multi-document AI assistant
* Persistent vector databases
* User authentication system
* Dashboard analytics
* Knowledge graph integration

---

# 👩‍💻 Author

Developed as part of a **Generative AI engineering project** demonstrating:

* Semantic search systems
* Vector databases
* Large Language Model integration
* AI-powered applications

---

# 📜 License

This project is licensed under the **MIT License**.

---

⭐ If you find this project useful, consider giving it a **star on GitHub**.
