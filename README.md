# 🚀 Auto-Apply Intelligence Suite (Batch Engine)

An autonomous multi-agent recruitment matching and executive outreach pipeline powered by **CrewAI**, **Google Gemini**, and **LiteLLM**. Features an interactive **Streamlit Telemetry UI**, deterministic multi-role batch processing, automated test suites via **Pytest**, and upcoming human-in-the-loop browser automation.

---

## 🌟 Key Highlights

* **Multi-Agent Orchestration**: 3 specialized agents executing sequential intelligence workflows:
  * **Precision Matcher**: Audits technical depth, calculates alignment percentages, and identifies skill gaps.
  * **Intel Researcher**: Investigates company architecture bottlenecks (token consumption, agent drift, latency).
  * **Executive Pitcher**: Drafts hyper-personalized outreach briefs tailored to engineering leaders.
* **Batch Processing Engine**: Evaluate multiple target companies and job descriptions simultaneously with zero manual context switching.
* **Streamlit Telemetry UI**: Single-view zero-scroll interface with both Light and Dark mode optimization.
* **Automated Testing Suite**: Full architectural test coverage implemented via **Pytest**.

---

## 🏗️ Architecture Flow

```text
[ Candidate Resume ] + [ Target Job Descriptions (1 to 5) ]
                         │
                         ▼
        ┌──────────────────────────────────┐
        │       1. Precision Matcher       │
        └──────────────────────────────────┘
                         │
                         ▼
        ┌──────────────────────────────────┐
        │       2. Intel Researcher        │
        └──────────────────────────────────┘
                         │
                         ▼
        ┌──────────────────────────────────┐
        │       3. Executive Pitcher       │
        └──────────────────────────────────┘
                         │
                         ▼
     [ Streamlit Dashboard / Batch Output Tabs ]
                         │
                         ▼
    [ Export Executive Pitches (.txt) / Selenium Automation ]
```

---

## 🛠️ Tech Stack

* **Core Framework**: CrewAI
* **LLM Engine**: Google Gemini Flash (via LiteLLM)
* **Frontend UI**: Streamlit
* **Automated Testing**: Pytest
* **Language & Runtime**: Python 3.11+ / 3.13

---

## ⚡ Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/satyanarayana51115/auto-apply-intelligence-suite.git](https://github.com/satyanarayana51115/auto-apply-intelligence-suite.git)
cd auto-apply-intelligence-suite
```

### 2. Configure Virtual Environment
```bash
python -m venv .venv
```

**On Windows:**
```bash
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run Test Suite
Verify that all core components and batch architectures pass:
```bash
pytest
```

### 6. Launch Application
* **Batch Multi-Company Engine (Recommended):**
  ```bash
  streamlit run batch_app.py
  ```
* **Single Role Telemetry App:**
  ```bash
  streamlit run app.py
  ```

---

## 📸 Output Preview

### Batch Engine Dashboard
![Batch Dashboard](assets/batch_preview.png)

---

## 🛡️ License
Distributed under the MIT License.
