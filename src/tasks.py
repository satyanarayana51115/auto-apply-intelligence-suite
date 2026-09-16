from crewai import Task

def create_matching_task(agent, resume_text, job_description):
    return Task(
        description=(
            f"Analyze the candidate resume against the given job description.\n\n"
            f"**Candidate Resume:**\n{resume_text}\n\n"
            f"**Job Description:**\n{job_description}\n\n"
            "Requirements:\n"
            "1. Calculate an ATS Match Score out of 100.\n"
            "2. List matching hard and soft skills.\n"
            "3. Identify top 3 critical missing keywords or skill gaps.\n"
            "4. Provide a clear 'Apply Recommendation': High Fit (>80%), Moderate Fit (60-80%), or Low Fit (<60%)."
        ),
        expected_output=(
            "A structured breakdown containing:\n"
            "- Overall Match Score (0-100)\n"
            "- Matched Skills List\n"
            "- Missing Critical Keywords / Gaps\n"
            "- Fit Recommendation verdict"
        ),
        agent=agent
    )

def create_intel_task(agent, company_name, job_description):
    return Task(
        description=(
            f"Analyze the role for company '{company_name}' based on this job description:\n\n"
            f"{job_description}\n\n"
            "Identify:\n"
            "1. Core business problems the team wants this role to solve.\n"
            "2. Expected key deliverables in the first 90 days.\n"
            "3. Ideal communication tone (e.g., startup direct, enterprise formal)."
        ),
        expected_output=(
            "A concise intelligence summary of the company's pain points and desired candidate strengths."
        ),
        agent=agent
    )

def create_pitch_task(agent, resume_text, job_description, company_name):
    return Task(
        description=(
            f"Draft a hyper-personalized 3-paragraph cold outreach message to the hiring manager at '{company_name}'.\n\n"
            f"Candidate profile highlights are derived from:\n{resume_text}\n\n"
            f"Target role:\n{job_description}\n\n"
            "Guidelines:\n"
            "- Paragraph 1: Hook citing a specific company priority and how candidate expertise matches.\n"
            "- Paragraph 2: Two concrete achievements proving capability (metrics/tools).\n"
            "- Paragraph 3: Direct, low-friction call-to-action (brief 10-minute sync).\n"
            "- Strictly avoid cliches like 'I hope this email finds you well'."
        ),
        expected_output=(
            "A high-impact, 3-paragraph outreach pitch ready to be dispatched via email or LinkedIn InMail."
        ),
        agent=agent
    )