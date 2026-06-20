from config import URL
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get(URL)

driver.save_screenshot("website.png")

driver.quit()