<div align="center">
  <h1>🧠 Self-Improving AI Agent</h1>
  <p><strong>An autonomous agent that leverages the Reflexion pattern and long-term memory to iteratively improve its performance.</strong></p>
</div>

## 🚀 Overview
The **Self-Improving AI Agent** moves beyond zero-shot execution. When given a complex task, it generates a solution, evaluates it against a success criteria (like a test suite), and if it fails, it generates a "Self-Reflection". This reflection acts as an internal critique, allowing the agent to correct its mistakes in the next iteration. Combined with a long-term Vector DB memory, the agent remembers past mistakes and avoids repeating them.

![Agent Trace Demo](/C:/Users/hp/.gemini/antigravity-ide/brain/fdf49048-b37f-4711-af04-f256131d4933/self_improving_agent_dashboard_1786416799454.png)

## ✨ Features
- **Reflexion Loop:** Iterative generation -> evaluation -> reflection -> retry cycle.
- **Long-Term Memory Integration:** Uses vector databases (Zep/Mem0) to recall past failures and successful strategies across different sessions.
- **Execution Trace UI:** A beautiful Streamlit dashboard that visualizes the agent's internal monologue and state transitions.
- **Dynamic Tasking:** Capable of handling coding challenges, logical puzzles, and data analysis tasks.

## 🛠️ Tech Stack
- **Agent Framework:** [LangGraph](https://python.langchain.com/v0.1/docs/langgraph/)
- **Frontend/UI:** [Streamlit](https://streamlit.io/)
- **LLM Engine:** OpenAI GPT-4o / Llama 3
- **Memory Store:** ChromaDB / SQLite Vector

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhammad08-dot/self-improving-ai-agent.git
   cd self-improving-ai-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit langgraph langchain chromadb
   ```

3. **Run the application:**
   ```bash
   streamlit run streamlit_app.py
   ```

## 📄 License
This project is licensed under the MIT License.
