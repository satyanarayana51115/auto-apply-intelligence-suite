import os
import streamlit as st
from dotenv import load_dotenv
from src.pipeline import run_batch_pipeline
from src.browser_agent import submit_autonomous_application

load_dotenv()

st.set_page_config(
    page_title="AutoApply Intelligence Suite - Batch Engine",
    page_icon="🚀",
    layout="wide"
)

# పర్ఫెక్ట్ హైట్ & సింగిల్ స్క్రీన్ కాంపాక్ట్ CSS
st.markdown("""
<style>
    .block-container { 
        padding-top: 3.6rem !important; 
        padding-bottom: 0.5rem !important; 
        max-width: 95% !important;
    }
    .header-box { 
        text-align: center; 
        margin-bottom: 8px; 
    }
    .main-title { 
        color: #2ecc71; 
        font-size: 1.75rem; 
        font-weight: 800; 
        line-height: 1.15;
        margin-bottom: 2px; 
    }
    .gold-sub { 
        color: #D4AC0D; 
        font-size: 0.9rem; 
        font-weight: 600; 
    }
    h3 { 
        margin-top: 0.1rem !important; 
        margin-bottom: 0.1rem !important; 
        font-size: 1.05rem !important; 
        font-weight: 700 !important;
    }
    .stTextInput > div > div > input {
        padding: 3px 8px !important;
        height: 34px !important;
        font-size: 0.88rem !important;
    }
    .stTextArea textarea {
        min-height: 38px !important;
        font-size: 0.86rem !important;
        line-height: 1.25 !important;
    }
    div[data-testid="stTextInput"], div[data-testid="stTextArea"] {
        margin-bottom: 2px !important;
    }
    button[data-baseweb="tab"] {
        font-weight: 700 !important;
        font-size: 0.85rem !important;
        padding: 2px 10px !important;
    }
    .stButton > button, .stDownloadButton > button {
        height: 36px !important;
        font-size: 0.84rem !important;
        font-weight: 600 !important;
    }
    div[data-testid="stAlert"] {
        padding: 3px 8px !important;
        margin-bottom: 4px !important;
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

if "persisted_results" not in st.session_state:
    st.session_state.persisted_results = None

# 1. కాండిడేట్ ప్రొఫైల్ వివరాలు
st.markdown("### Candidate Technical Profile")
col_p1, col_p2, col_p3 = st.columns([1.2, 1.2, 1])
with col_p1:
    cand_name = st.text_input("Candidate Name", value="Satya Raj")
with col_p2:
    cand_email = st.text_input("Candidate Email", value="raj.ai.engineer@example.com")
with col_p3:
    cand_phone = st.text_input("Candidate Phone", value="9876543210")

default_profile = (
    "Python Developer with 5+ years experience building CrewAI agents, "
    "LiteLLM orchestration, RAG pipelines, and automated intelligence workflows."
)
candidate_profile = st.text_area(
    "Profile Summary & Core Competencies:",
    value=default_profile,
    height=38
)

# 2. టార్గెట్ కంపెనీల ఎంపిక
col_head, col_slider = st.columns([1.6, 2.4])
with col_head:
    st.markdown("### Target Companies & Job Roles")
with col_slider:
    num_jobs = st.slider("Select number of companies to evaluate:", min_value=1, max_value=5, value=1)

job_tabs = st.tabs([f"Job #{i+1}" for i in range(num_jobs)])
jobs_input = []

for i, tab in enumerate(job_tabs):
    with tab:
        col_c, col_d = st.columns([1, 2])
        with col_c:
            c_name = st.text_input(f"Target Company #{i+1}", value=f"Company {chr(65+i)}", key=f"comp_{i}")
        with col_d:
            jd_text = st.text_area(
                f"Job Requirements / Description #{i+1}",
                value=f"Seeking an Engineer skilled in Python, Agentic AI, API integration, and performance optimization for {c_name}.",
                height=38,
                key=f"jd_{i}"
            )
        jobs_input.append({"company": c_name, "description": jd_text})

# 3. రన్ బటన్
if st.button("🚀 Run Batch Intelligence Pipeline", type="primary", use_container_width=True):
    if not candidate_profile.strip():
        st.error("Please provide the candidate technical profile before launching.")
    else:
        with st.spinner("Processing targets..."):
            try:
                results = run_batch_pipeline(candidate_profile, jobs_input)
                st.session_state.persisted_results = results
            except Exception as e:
                st.error(f"Batch Processing Error: {str(e)}")

# 4. ఫలితాలు & 3 బటన్లు ఒకే హారిజాంటల్ లైన్‌లో
if st.session_state.persisted_results:
    results = st.session_state.persisted_results
    st.success(f"🎉 Successfully processed {len(results)} target role(s)!")

    out_tabs = st.tabs([f"{res['company']}" for res in results])
    all_pitches = ""
    for r in results:
        all_pitches += f"=== {r['company']} Executive Pitch ===\n{r['output']}\n\n"

    for idx, tab in enumerate(out_tabs):
        with tab:
            res = results[idx]
            st.text_area(
                f"Generated Pitch ({res['company']})",
                value=res['output'],
                height=110,
                key=f"out_area_{idx}"
            )
            
            # ఆ 3 బటన్లు ఒకే సమాంతర లైన్‌లో (Horizontal Row)
            b1, b2, b3 = st.columns([1, 1.15, 1.2])
            with b1:
                st.download_button(
                    label=f"📥 Download ({res['company']})",
                    data=res['output'],
                    file_name=f"{res['company']}_pitch.txt",
                    mime="text/plain",
                    key=f"dl_single_btn_{idx}",
                    use_container_width=True
                )
            with b2:
                if st.button(f"🤖 Auto-Fill ({res['company']})", key=f"autofill_btn_{idx}", use_container_width=True):
                    with st.spinner(f"Auto-filling application for {res['company']}..."):
                        shot_path = submit_autonomous_application(
                            candidate_name=cand_name,
                            email=cand_email,
                            phone=cand_phone,
                            company_name=res['company'],
                            pitch_text=res['output']
                        )
                        st.success(f"Proof saved: {shot_path}")
                        st.image(shot_path, caption=f"Proof - {res['company']}", width=420)
            with b3:
                st.download_button(
                    label="📦 Download All Pitches (.txt)",
                    data=all_pitches,
                    file_name="All_Companies_Executive_Pitches.txt",
                    mime="text/plain",
                    key=f"dl_all_btn_{idx}",
                    use_container_width=True
                )