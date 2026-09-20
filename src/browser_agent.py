import os
import time
from playwright.sync_api import sync_playwright

def submit_autonomous_application(candidate_name: str, email: str, phone: str, company_name: str, pitch_text: str):
    """
    Playwright బ్రౌజర్ ఆటోమేషన్ ద్వారా అప్లికేషన్ ఫారమ్‌ను ఫిల్ చేసి స్క్రీన్‌షాట్ తీస్తుంది.
    """
    os.makedirs("application_proofs", exist_ok=True)
    screenshot_path = f"application_proofs/{company_name.lower().replace(' ', '_')}_applied.png"

    with sync_playwright() as p:
        # headless=False వల్ల బ్రౌజర్ ప్రత్యక్షంగా స్క్రీన్ మీద ఓపెన్ అవుతుంది
        browser = p.chromium.launch(headless=False, slow_mo=700)
        page = browser.new_page()

        # డెమో అప్లికేషన్ పోర్టల్
        page.goto("https://httpbin.org/forms/post")

        # ఫీల్డ్స్ ఆటోమేటెడ్ ఎంట్రీ
        page.fill('input[name="custname"]', candidate_name)
        page.fill('input[name="custtel"]', phone)
        page.fill('input[name="custemail"]', email)
        
        # ఏజెంట్ జనరేట్ చేసిన కస్టమ్ ఎగ్జిక్యూటివ్ పిచ్ ఇక్కడ ఇన్సర్ట్ అవుతుంది
        formatted_pitch = f"[{company_name} Role Submission]\n{pitch_text}"
        page.fill('textarea[name="comments"]', formatted_pitch)

        # స్క్రీన్‌షాట్ ద్వారా ప్రూఫ్ క్యాప్చర్
        page.screenshot(path=screenshot_path)
        
        time.sleep(2)
        browser.close()

    return screenshot_path