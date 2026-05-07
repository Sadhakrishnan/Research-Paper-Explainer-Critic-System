import streamlit as st
import requests
import os
import json

# Set page config for a premium feel
st.set_page_config(
    page_title="Research Paper Explainer + Critic",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for modern look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .report-card {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .source-tag {
        font-size: 0.8em;
        background-color: #e9ecef;
        padding: 2px 8px;
        border-radius: 12px;
        margin-right: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

API_URL = "http://localhost:8000"

st.title("🔬 Research Paper Explainer + Critic")
st.markdown("---")

# Sidebar for Upload and Settings
with st.sidebar:
    st.header("📂 Ingestion")
    uploaded_file = st.file_uploader("Upload a Research Paper (PDF)", type=["pdf"])
    
    if uploaded_file:
        if st.button("🚀 Process Paper"):
            with st.spinner("Analyzing paper structure and creating vector index..."):
                files = {"file": uploaded_file.getvalue()}
                # We need to send the filename too, but streamlit file_uploader returns a BytesIO-like object
                # For simplicity in this demo, we'll use a fixed name or handle it via requests
                response = requests.post(f"{API_URL}/upload", files={"file": (uploaded_file.name, uploaded_file.getvalue())})
                if response.status_code == 200:
                    st.success("Paper processed successfully!")
                    st.session_state["filename"] = uploaded_file.name
                    st.session_state["sections"] = response.json().get("sections", [])
                else:
                    st.error(f"Error: {response.text}")

    if "sections" in st.session_state:
        st.subheader("Detected Sections")
        for section in st.session_state["sections"]:
            st.write(f"- {section}")

# Main Interaction Area
if "filename" in st.session_state:
    st.header(f"Analyzing: {st.session_state['filename']}")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📝 Explain", "👶 Simplify", "🔍 Critique", "📚 Citations"])
    
    with tab1:
        st.subheader("Explain the Paper")
        q_explainer = st.text_input("What would you like to know?", value="What is the core contribution of this paper?", key="exp_q")
        if st.button("Generate Explanation", key="exp_btn"):
            with st.spinner("Consulting Explainer Agent..."):
                res = requests.post(f"{API_URL}/ask", params={"filename": st.session_state["filename"], "question": q_explainer, "agent_type": "explainer"})
                if res.status_code == 200:
                    data = res.json()
                    st.markdown(f"<div class='report-card'>{data['answer']}</div>", unsafe_allow_html=True)
                    with st.expander("Sources"):
                        for src in data["sources"]:
                            st.markdown(f"**Page {src['metadata']['page']} ({src['metadata']['section']})**")
                            st.info(src["content"])
                else:
                    st.error("Failed to get answer from API.")

    with tab2:
        st.subheader("Simplify Concepts")
        q_simplifier = st.text_input("Which concept should I simplify?", value="Explain the methodology in simple terms.", key="sim_q")
        if st.button("Simplify", key="sim_btn"):
            with st.spinner("Consulting Simplifier Agent..."):
                res = requests.post(f"{API_URL}/ask", params={"filename": st.session_state["filename"], "question": q_simplifier, "agent_type": "simplifier"})
                if res.status_code == 200:
                    data = res.json()
                    st.markdown(f"<div class='report-card'>{data['answer']}</div>", unsafe_allow_html=True)
                else:
                    st.error("Failed to get answer from API.")

    with tab3:
        st.subheader("Critique Methodology")
        q_critic = st.text_input("Specific area to critique?", value="Are there any weak assumptions or missing baselines?", key="cri_q")
        if st.button("Analyze Weaknesses", key="cri_btn"):
            with st.spinner("Consulting Critic Agent..."):
                res = requests.post(f"{API_URL}/ask", params={"filename": st.session_state["filename"], "question": q_critic, "agent_type": "critic"})
                if res.status_code == 200:
                    data = res.json()
                    st.markdown(f"<div class='report-card'>{data['answer']}</div>", unsafe_allow_html=True)
                else:
                    st.error("Failed to get answer from API.")

    with tab4:
        st.subheader("Citation Tracking")
        if st.button("Extract Citations", key="cit_btn"):
            with st.spinner("Consulting Citation Agent..."):
                res = requests.post(f"{API_URL}/ask", params={"filename": st.session_state["filename"], "question": "Extract all references and where they are used.", "agent_type": "citation"})
                if res.status_code == 200:
                    data = res.json()
                    st.markdown(f"<div class='report-card'>{data['answer']}</div>", unsafe_allow_html=True)
                else:
                    st.error("Failed to get answer from API.")

else:
    st.info("Please upload a research paper to begin analysis.")
    st.image("https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Intelligent Literature Analysis")

st.markdown("---")
st.caption("Built with ❤️ using LangChain, FAISS, and FastAPI")
