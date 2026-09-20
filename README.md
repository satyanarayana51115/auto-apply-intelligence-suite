# 🚀 Auto-Apply Intelligence Suite

An autonomous multi-agent AI system designed to bridge the gap between candidate qualifications and technical job requirements. Built with **CrewAI**, **LiteLLM / Google Gemini**, **Streamlit**, and **Playwright**, the system performs multi-company ATS gap analysis, generates tailored high-impact executive pitches, and autonomously applies through browser automation with verified execution proofs.

---

## 🏗️ Architecture Overview

```text
                          [ Candidate Technical Profile ]
                                         │
                                         ▼
                     ┌───────────────────────────────────────┐
                     │     Target Roles (Batch Engine)       │
                     └───────────────────┬───────────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
     ┌────────────────────────┐                     ┌────────────────────────┐
     │  Job 1 (Company A)     │                     │  Job 2 (Company B)     │
     └───────────┬────────────┘                     └───────────┬────────────┘
                 │                                               │
                 ▼                                               ▼
  [ CrewAI Multi-Agent Pipeline ]                 [ CrewAI Multi-Agent Pipeline ]
  • Requirements Extraction                       • Requirements Extraction
  • Technical Gap Analysis                        • Technical Gap Analysis
  • Executive Pitch Generator                     • Executive Pitch Generator
                 │                                               │
                 └───────────────────────┬───────────────────────┘
                                         │
                                         ▼
                     ┌───────────────────────────────────────┐
                     │ Streamlit Batch Dashboard (Persistent)│
                     └───────────────────┬───────────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
     [ Single & Bulk TXT Exports ]                 [ Playwright Autonomous Apply ]
                                                   • Headless / Managed Browser
                                                   • Autonomous Form Filling
                                                   • Visual Verification Screenshot
```                                         

## ✨ Key Engineering Features

* **​Autonomous Multi-Company Batch Evaluation:** 
    Analyzes multiple job targets concurrently using dedicated CrewAI agent workflows without UI state reset.

* **​Production-Calibrated Output:**
    Pitches are structured with bold executive highlights, quantitative performance metrics (e.g., latency reduction, token economics, API reliability), and direct calls to action.

​* **Playwright Autonomous Application:**
    Automatically launches the browser, populates application form fields with candidate metadata and tailored pitches, and records execution proofs.

​* **State Persistence & Clean UX:**
    Custom CSS styling optimized for zero-scroll single-window operations, preserving state and download actions across re-renders.

​* **Automated Verification:**
    Comprehensive test suite implemented via pytest validating browser automation reliability and artifact creation.


​## 📁 Repository Structure

```text
auto-apply-intelligence-suite/
├── application_proofs/          # Execution screenshots from Playwright automation
├── src/
│   ├── agents.py                # CrewAI agent definitions & configurations
│   ├── tasks.py                 # Task prompts & evaluation logic
│   ├── pipeline.py              # Batch execution orchestration pipeline
│   └── browser_agent.py         # Playwright autonomous browser filling logic
├── tests/
│   └── test_browser_agent.py    # Pytest automated test coverage
├── test_browser.py              # Standalone Playwright verification script
├── app.py                       # Single-role Streamlit dashboard
├── batch_app.py                 # Multi-company batch intelligence engine
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation

```
## ⚡ Quickstart & Setup

1. **Clone & Environment Setup**
```
git clone https://github.com/satyanarayana51115/auto-apply-intelligence-suite.git
cd auto-apply-intelligence-suite
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```
2. **Configure Environment Variables**
   Create a .env file in the root directory:

```
GEMINI_API_KEY=your_google_gemini_api_key
```

3. **Launch the Application**

```
streamlit run batch_app.py
```

4. **Run Automated Tests**

```
pytest -v
```


