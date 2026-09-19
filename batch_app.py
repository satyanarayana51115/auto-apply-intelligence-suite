import os
import streamlit as st
from dotenv import load_dotenv
from src.pipeline import run_batch_pipeline

load_dotenv()

st.set_page_config(
    page_title="AutoApply Intelligence Suite - Batch Engine",
    page_icon="🚀",
    layout="wide"
)

# లేఅవుట్ & స్టైలింగ్
st.markdown("""
<style>
    .block-container { 
        padding-top: 3.2rem !important; 
        padding-bottom: 2rem !important; 
        max-width: 95% !important;
    }
    .header-box { 
        text-align: center; 
        margin-bottom: 18px; 
    }
    .main-title { 
        color: #2ecc71; 
        font-size: 2.1rem; 
        font-weight: 800; 
        line-height: 1.2;
        letter-spacing: 0.5px;
        margin-bottom: 4px; 
    }
    .gold-sub { 
        color: #D4AC0D; 
        font-size: 1.05rem; 
        font-weight: 600; 
        letter-spacing: 0.5px; 
    }
    h3 { 
        margin-top: 0.4rem !important; 
        margin-bottom: 0.3rem !important; 
        font-size: 1.2rem !important; 
        font-weight: 700 !important;
    }
    button[data-baseweb="tab"] {
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        padding: 6px 16px !important;
        margin-right: 6px !important;
    }
</style>
<div class="header-box">
    <div class="main-title">🚀 Auto-Apply Intelligence Suite (Batch Engine)</div>
    <div class="gold-sub">Autonomous Multi-Company ATS Matching & Executive Pitch Generation</div>
</div>
""", unsafe_allow_html=True)

if not os.getenv("GEMINI_API_KEY"):
    st.error("⚠️ GEMINI_API_KEY environment variable is missing. Please verify your .env file.")
    st.stop()

# సెషన్ స్టేట్ లో రిజల్ట్స్ భద్రపరచడానికి వేరియబుల్
if "batch_results" not in st.session_state:
    st.session_state.batch_results = None

# 1. కాండిడేట్ ప్రొఫైల్
st.markdown("### Candidate Technical Profile")
default_profile = (
    "Python Developer with 5+ years experience building CrewAI agents, "
    "LiteLLM orchestration, RAG pipelines, and automated intelligence workflows."
)
candidate_profile = st.text_area(
    "Profile Summary & Core Competencies:",
    value=default_profile,
    height=90,
    help="Enter resume highlights, technical skills, and core engineering focus."
)

st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

# 2. టార్గెట్ కంపెనీలు & స్లైడర్
col_head, col_slider = st.columns([1.6, 2.4])
with col_head:
    st.markdown("### Target Companies & Job Roles")
with col_slider:
    num_jobs = st.slider("Select number of companies to evaluate:", min_value=1, max_value=5, value=2)

job_tabs = st.tabs([f"Job #{i+1}" for i in range(num_jobs)])
jobs_input = []

for i, tab in enumerate(job_tabs):
    with tab:
        col_c, col_d = st.columns([1, 2])
        with col_c:
            c_name = st.text_input(
                f"Target Company #{i+1}",
                value=f"Company {chr(65+i)}",
                key=f"comp_{i}"
            )
        with col_d:
            jd_text = st.text_area(
                f"Job Requirements / Description #{i+1}",
                value=f"Seeking an Engineer skilled in Python, Agentic AI, API integration, and performance optimization for {c_name}.",
                height=95,
                key=f"jd_{i}"
            )
        jobs_input.append({"company": c_name, "description": jd_text})

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

# రన్ బటన్
if st.button("🚀 Run Batch Intelligence Pipeline", type="primary", use_container_width=True):
    if not candidate_profile.strip():
        st.error("Please provide the candidate technical profile before launching the pipeline.")
    else:
        with st.spinner(f"Agents are actively analyzing requirements for {num_jobs} companies... Please wait..."):
            try:
                results = run_batch_pipeline(candidate_profile, jobs_input)
                # ఫలితాలను session_state లో శాశ్వతంగా ఉంచుతున్నాం
                st.session_state.batch_results = results
                st.rerun()
            except Exception as e:
                st.error(f"Batch Processing Error: {str(e)}")

# ఫలితాలు ఉంటే వాటిని డిస్‌ప్లే చేయడం (డౌన్‌లోడ్ చేసినా ఇవి మాయమవ్వవు)
if st.session_state.batch_results:
    results = st.session_state.batch_results
    st.success(f"🎉 Successfully processed {len(results)} target roles!")

    out_tabs = st.tabs([f"{res['company']}" for res in results])
    all_pitches = ""

    for idx, tab in enumerate(out_tabs):
        with tab:
            res = results[idx]
            st.markdown(f"#### Pitch & Brief for {res['company']}")
            st.text_area(
                f"Generated Output ({res['company']})",
                value=res['output'],
                height=220,
                key=f"res_{idx}"
            )
            st.download_button(
                label=f"📥 Download Pitch ({res['company']})",
                data=res['output'],
                file_name=f"{res['company']}_pitch.txt",
                mime="text/plain",
                key=f"dl_{idx}"
            )
            all_pitches += f"=== {res['company']} Executive Pitch ===\n{res['output']}\n\n"

    st.markdown("<div style='margin-top: 12px;'></div>", unsafe_allow_html=True)
    st.download_button(
        label="📦 Download All Executive Pitches (.txt)",
        data=all_pitches,
        file_name="All_Companies_Executive_Pitches.txt",
        mime="text/plain",
        key=f"dl_all"
    )