from crewai import Crew, Process
from src.agents import (
    create_matcher_agent,
    create_intel_agent,
    create_copywriter_agent
)
from src.tasks import (
    create_matching_task,
    create_intel_task,
    create_pitch_task
)

class AutoApplyIntelligenceSuite:
    def __init__(self):
        self.matcher = create_matcher_agent()
        self.intel_agent = create_intel_agent()
        self.copywriter = create_copywriter_agent()

    def run_suite(self, resume_text: str, job_description: str, company_name: str) -> dict:
        # Define tasks for each agent
        match_task = create_matching_task(self.matcher, resume_text, job_description)
        intel_task = create_intel_task(self.intel_agent, company_name, job_description)
        pitch_task = create_pitch_task(self.copywriter, resume_text, job_description, company_name)

        # Assemble the sequential Crew
        crew = Crew(
            agents=[self.matcher, self.intel_agent, self.copywriter],
            tasks=[match_task, intel_task, pitch_task],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        return {
            "execution_status": "Success",
            "full_output": str(result)
        }

if __name__ == "__main__":
    # Quick sanity test block
    sample_resume = "Python Developer with 5+ years experience building CrewAI agents, LiteLLM integrations, and RAG pipelines."
    sample_jd = "Looking for an Agentic AI Engineer proficient in Python, CrewAI, LLM workflow automation, and Prompt Engineering."
    company = "Talentgigs"

    print("\n[+] Initializing Auto-Apply Intelligence Suite...\n")
    suite = AutoApplyIntelligenceSuite()
    output = suite.run_suite(sample_resume, sample_jd, company)
    print("\n--- EXECUTION OUTPUT ---\n")
    print(output["full_output"])

def run_batch_pipeline(candidate_profile, jobs_list):
    suite = AutoApplyIntelligenceSuite()
    run_func = getattr(suite, "run_suite", getattr(suite, "run", None))
    
    batch_results = []
    for index, job in enumerate(jobs_list, 1):
        company_name = job.get("company", f"Company #{index}")
        job_desc = job.get("description", "")
        
        # కీవర్డ్ ఆర్గ్యుమెంట్ కాకుండా నేరుగా పొజిషనల్ ఆర్గ్యుమెంట్లుగా పంపడం
        try:
            res = run_func(candidate_profile, job_desc, company_name)
        except TypeError:
            res = run_func(candidate_profile, job_desc)
        
        # ఫలితం డిక్షనరీ అయినా లేదా ఆబ్జెక్ట్ అయినా టెక్స్ట్‌ను సురక్షితంగా తీసుకోవడం
        out_text = res.get("full_output", str(res)) if isinstance(res, dict) else str(res)
        
        batch_results.append({
            "company": company_name,
            "output": out_text
        })
    return batch_results