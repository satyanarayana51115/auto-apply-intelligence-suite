import os
from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

# Gemini LLM Setup via CrewAI / LiteLLM format
gemini_llm = LLM(
    model="gemini/gemini-3.6-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3
)

def create_matcher_agent():
    return Agent(
        role="ATS Precision Job Match Analyst",
        goal="Evaluate candidate resumes strictly against job descriptions and determine quantitative match fit.",
        backstory=(
            "You are an elite enterprise technical recruiter and ATS evaluation engine. "
            "You calculate precise alignment percentages, extract exact skill gaps, "
            "and provide actionable insights without fluff or exaggeration."
        ),
        llm=gemini_llm,
        verbose=True
    )

def create_intel_agent():
    return Agent(
        role="Corporate Intelligence & Recruiter Profiler",
        goal="Analyze target company domain, technical focus, and potential organizational pain points.",
        backstory=(
            "You are a specialized corporate intelligence researcher. "
            "You quickly determine what engineering problems a hiring team is facing "
            "and identify the exact technical value an applicant must demonstrate."
        ),
        llm=gemini_llm,
        verbose=True
    )

def create_copywriter_agent():
    return Agent(
        role="Executive Career Strategist & Cold Pitch Specialist",
        goal="Draft high-conversion, hyper-personalized outreach messages and custom cover notes.",
        backstory=(
            "You are a high-level executive talent agent. You write concise, high-impact "
            "inmail and cold email pitches directly to founders and hiring managers. "
            "You never use generic templates or robotic cliches."
        ),
        llm=gemini_llm,
        verbose=True
    )