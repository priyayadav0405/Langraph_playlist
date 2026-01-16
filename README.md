# 🤖 LangGraph Playlist Chatbot

> A powerful conversational AI chatbot built with **LangGraph** and **Streamlit** featuring real-time interactions and persistent message history.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-Active-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ✨ Features

- 💬 **Real-time Conversational AI** - Powered by LangGraph for intelligent responses
- 📝 **Message History** - Persistent chat history within each session
- 🎨 **Beautiful UI** - Clean, intuitive Streamlit interface
- 🔄 **Thread-based Sessions** - Unique thread IDs for conversation tracking
- ⚡ **Fast & Responsive** - Instant message processing and responses
- 🛡️ **Error Handling** - Robust error management with user-friendly messages

---

## 📋 Requirements

- Python 3.8 or higher
- pip package manager
- Internet connection for API calls

---

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd Langraph_playlist
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### Step 3: Install Dependencies
```bash
pip install streamlit langchain langgraph langchain-core
```

### Step 4: Set Environment Variables
```bash
# Create a .env file if needed for API keys
OPENAI_API_KEY=your_key_here
```

---

## 📖 Usage

### Running the Application
```bash
streamlit run langgraph_frontend.py
```

The app will open automatically at `http://localhost:8501`

### How to Chat
1. Type your message in the input field
2. Press Enter or click Send
3. Wait for the AI response
4. Chat history is automatically saved
5. Click "Clear Chat" to reset the conversation

---

## 🏗️ Project Structure

```
Langraph_playlist/
├── 📄 langgraph_frontend.py    # Streamlit UI & frontend logic
├── 📄 langgraph_backend_1.py   # LangGraph chatbot logic
└── 📄 README.md                 # Project documentation
```

---

## 🔧 Technical Architecture

### Frontend (`langgraph_frontend.py`)
- Streamlit-based user interface
- Session state management for message history
- Chat message display with role-based styling
- User input handling and processing

### Backend (`langgraph_backend_1.py`)
- LangGraph graph construction
- Conversation flow orchestration
- Message processing and response generation
- Thread-based session management

### State Management
- **Session State**: Stores `message_history` list for persistent chat
- **Thread ID**: Unique identifier (`thread_1`) for conversation tracking
- **Config**: Configuration dictionary for graph invocation

---

## 💡 How It Works

```
User Input
    ↓
Streamlit UI (langgraph_frontend.py)
    ↓
LangGraph Backend (langgraph_backend_1.py)
    ↓
AI Processing & Response Generation
    ↓
Display Response in Chat
    ↓
Update Message History
```

---

## 🎯 Key Functions

| Function | Purpose |
|----------|---------|
| `st.chat_input()` | Captures user messages |
| `st.chat_message()` | Displays messages with role styling |
| `chatbot.invoke()` | Sends message to LangGraph backend |
| `st.session_state` | Maintains message history |

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Import errors | Run `pip install -r requirements.txt` |
| API Key errors | Check `.env` file and API key validity |
| Port already in use | Run `streamlit run app.py --server.port 8502` |
| Slow responses | Check internet connection and API rate limits |

---

## 📦 Dependencies

```
streamlit>=1.28.0
langchain>=0.1.0
langgraph>=0.0.1
langchain-core>=0.1.0
python-dotenv>=1.0.0
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-xxxxx
LANGCHAIN_API_KEY=lsk-xxxxx
```

---

## 📝 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📧 Support & Contact

For questions, issues, or suggestions:
- Open an [Issue](https://github.com/yourusername/langraph-playlist/issues)
- Contact: your-email@example.com

---

## 🙏 Acknowledgments

- Built with [LangGraph](https://langgraph.readthedocs.io/)
- UI powered by [Streamlit](https://streamlit.io/)
- Language models via [LangChain](https://langchain.readthedocs.io/)

---

**Made with ❤️ by [Your Name]**