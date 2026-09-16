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