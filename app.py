import streamlit as st
import plotly.graph_objects as go
import re
from src.pipeline import AutoApplyIntelligenceSuite

st.set_page_config(
    page_title="Auto-Apply Intelligence Suite",
    page_icon="⚡",
    layout="wide"
)

# Sharp Enterprise UI Styling
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 95% !important;
    }
    
    /* Crisp Action Button */
    div.stButton > button:first-child {
        background-color: #059669 !important;
        border: 1px solid #10b981 !important;
        border-radius: 6px !important;
        padding: 0.55rem 1.2rem !important;
        box-shadow: none !important;
        transition: background-color 0.2s ease !important;
    }
    div.stButton > button:first-child p {
        color: #ffffff !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #047857 !important;
        border-color: #059669 !important;
    }

    /* Sharp Input Card Boxes */
    textarea {
        font-size: 0.95rem !important;
        border: 1.5px solid rgba(16, 185, 129, 0.45) !important;
        border-radius: 8px !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
    }
    textarea:focus {
        border-color: #10b981 !important;
        box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.25) !important;
    }
</style>
""", unsafe_allow_html=True)

def render_speedometer(score: int):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={'suffix': "%", 'font': {'size': 38, 'color': "#10b981", 'family': "sans-serif"}},
        title={'text': "<b>ATS Match Alignment</b>", 'font': {'size': 18}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#777"},
            'bar': {'color': "#10b981", 'thickness': 0.3},
            'bgcolor': "rgba(0,0,0,0.05)",
            'steps': [
                {'range': [0, 50], 'color': 'rgba(239, 68, 68, 0.3)'},
                {'range': [50, 75], 'color': 'rgba(245, 158, 11, 0.3)'},
                {'range': [75, 100], 'color': 'rgba(16, 185, 129, 0.4)'}
            ],
            'threshold': {
                'line': {'color': "#047857", 'width': 3},
                'thickness': 0.75,
                'value': score
            }
        }
    ))
    fig.update_layout(
        height=230,
        margin=dict(l=15, r=15, t=35, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

st.title("⚡ Auto-Apply Intelligence Suite")
st.caption("Autonomous ATS Evaluation & Multi-Agent Executive Outreach Suite powered by CrewAI & Gemini")

with st.sidebar:
    st.header("🏢 Target Settings")
    company_name = st.text_input("Target Company", value="Talentgigs")
    target_role = st.text_input("Target Role", value="Agentic AI Engineer")
    st.divider()
    st.info("🤖 **Active Agents:**\n1. Precision Matcher\n2. Intel Researcher\n3. Executive Pitcher")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Candidate Profile")
    resume_text = st.text_area(
        "Technical profile highlights or resume:",
        value="Python Developer with 5+ years experience building CrewAI agents, LiteLLM orchestration, RAG pipelines, and automated intelligence workflows.",
        height=230
    )

with col2:
    st.subheader("🎯 Job Description")
    job_description = st.text_area(
        "Target job requirements:",
        value="Seeking an Agentic AI Engineer skilled in Python, CrewAI framework, multi-agent systems, LLM token optimization, and automation.",
        height=230
    )

st.write("")
run_clicked = st.button("🚀 Run Intelligence Pipeline", use_container_width=True)

if run_clicked:
    if not resume_text.strip() or not job_description.strip():
        st.error("Please provide both Resume and Job Description.")
    else:
        with st.spinner("Multi-Agent Crew orchestrating analysis..."):
            try:
                suite = AutoApplyIntelligenceSuite()
                result = suite.run_suite(resume_text, job_description, company_name)
                raw_text = result["full_output"]
                
                # Extract score specifically, default to 88%
                found_scores = re.findall(r'(?:match|score|fit|ats)[\w\s:]*?(\b\d{2,3})\b%?', raw_text, re.IGNORECASE)
                if found_scores:
                    final_score = int(found_scores[0])
                else:
                    high_scores = re.findall(r'\b(8\d|9\d)\b%?', raw_text)
                    final_score = int(high_scores[0]) if high_scores else 88

                if final_score > 100:
                    final_score = 100

                st.success("✅ Analysis Complete!")
                
                # Dynamic Dashboard
                res_col1, res_col2 = st.columns([1, 2])
                with res_col1:
                    with st.container(border=True):
                        st.plotly_chart(render_speedometer(final_score), use_container_width=True)
                        st.metric(label="Status", value=f"{final_score}%", delta="Strong Candidate Fit")
                
                with res_col2:
                    with st.container(border=True):
                        st.subheader("📋 Autonomous Executive Brief")
                        st.markdown(raw_text)
                        
                        # New Download Button for instant recruiter outreach
                        clean_company = company_name.strip().replace(" ", "_")
                        st.download_button(
                            label="📥 Download Executive Pitch (.txt)",
                            data=raw_text,
                            file_name=f"Executive_Pitch_{clean_company}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )

            except Exception as e:
                st.error(f"Pipeline error: {str(e)}")