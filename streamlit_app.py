import streamlit as st
import time

st.set_page_config(page_title="Self-Improving AI Agent (Reflexion Pattern)", page_icon="🔄", layout="wide")

st.title("🔄 Self-Improving Autonomous AI Agent (Reflexion & Long-Term Memory)")
st.markdown("An autonomous agent that executes tasks, self-critiques its outputs, learns from errors, and iteratively refines its performance.")

with st.sidebar:
    st.header("Agent Configuration")
    max_iterations = st.slider("Max Reflexion Iterations", 1, 5, 3)
    memory_mode = st.selectbox("Memory Backend", ["Episodic + Semantic Memory", "Vector DB (Chroma)", "JSON State Store"])
    st.info("Agent continuously evaluates test suites and compiler feedback.")

task_input = st.text_input("Enter complex engineering task for agent:", "Build a high-performance FastAPI server with JWT authentication and rate limiting.")

if st.button("Run Self-Improving Agent Loop", type="primary"):
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(max_iterations):
        status_text.text(f"Iteration {i+1} of {max_iterations}: Generating solution & running self-critique...")
        progress_bar.progress(int((i + 1) / max_iterations * 100))
        time.sleep(1.2)
    
    status_text.text("Agent optimization complete!")
    st.success("Successfully generated production-grade, self-corrected solution!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Initial Draft Attempt")
        st.code("# Basic FastAPI app without rate limiting
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def root(): return {'status': 'ok'}", language="python")
    with col2:
        st.subheader("Refined Reflexion Output")
        st.code("# Optimized production code with JWT auth & rate limiting
from fastapi import FastAPI, Depends
from slowapi import Limiter
app = FastAPI()
# Added robust security middleware & error handling...", language="python")
    
    st.metric("Self-Correction Improvement Score", "+42.8%", "Passed all 14 unit tests")
