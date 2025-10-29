from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options (headless mode)
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Setup Chrome driver service
service = Service(ChromeDriverManager().install())

# Create driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open your Flask app
driver.get("http://localhost:5000")

# Wait for the page to load
time.sleep(2)

# Check if a quote is displayed
quote_text = driver.find_element("tag name", "h1").text
assert quote_text != ""

print("✅ Test passed: Quote displayed successfully!")

driver.quit()
