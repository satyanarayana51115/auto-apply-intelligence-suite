import os
import pytest
from src.browser_agent import submit_autonomous_application

def test_browser_agent_execution(tmp_path):
    """
    Playwright బ్రౌజర్ ఏజెంట్ ఫారమ్‌ను ఫిల్ చేసి స్క్రీన్‌షాట్ సరిగ్గా తీస్తోందో లేదో పరీక్షిస్తుంది.
    """
    candidate_name = "Test Candidate"
    email = "test@example.com"
    phone = "1234567890"
    company_name = "TestCompany"
    pitch_text = "Experienced AI Engineer specializing in autonomous workflows."

    screenshot_path = submit_autonomous_application(
        candidate_name=candidate_name,
        email=email,
        phone=phone,
        company_name=company_name,
        pitch_text=pitch_text
    )

    # స్క్రీన్‌షాట్ ఫైల్ క్రియేట్ అయిందా లేదా ధృవీకరించడం
    assert os.path.exists(screenshot_path), "Proof screenshot was not created!"
    assert screenshot_path.endswith(".png"), "Screenshot file format is not PNG!"