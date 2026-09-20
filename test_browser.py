import time
from playwright.sync_api import sync_playwright

def test_autonomous_browser():
    print("[+] Launching Autonomous Browser...")
    with sync_playwright() as p:
        # headless=False పెట్టడం వల్ల బ్రౌజర్ స్క్రీన్ మీద ఓపెన్ అవ్వడం ప్రత్యక్షంగా కనిపిస్తుంది
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        
        # ఒక టెస్ట్ డెమో జాబ్/అప్లికేషన్ పేజీకి వెళ్లడం
        print("[+] Navigating to test application page...")
        page.goto("https://httpbin.org/forms/post")
        
        # ఫారమ్ ఫీల్డ్స్‌ను ఆటోమేటిక్‌గా ఫిల్ చేయడం
        print("[+] Auto-filling candidate details...")
        page.fill('input[name="custname"]', "Satya Raj")
        page.fill('input[name="custtel"]', "9876543210")
        page.fill('input[name="custemail"]', "raj.ai.engineer@example.com")
        page.fill('textarea[name="comments"]', "Autonomous pitch: Python & CrewAI specialist applied via AutoApply Suite.")
        
        print("[+] Taking screenshot of automated form entry...")
        page.screenshot(path="browser_test_success.png")
        
        time.sleep(3)
        browser.close()
        print("🎉 Browser automation test executed successfully!")

if __name__ == "__main__":
    test_autonomous_browser()