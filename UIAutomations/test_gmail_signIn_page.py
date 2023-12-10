import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def test_goto_gmail_page():

    CHROME_DRIVER_PATH = r'C:\Users\prasa\Downloads\Compressed\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    PYTHON_URL = "https://www.google.com/gmail/about/"
    service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get(PYTHON_URL)
    delay = 0
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))).click()
        print("Page is ready!")
        # Read multiple css selector text
        Readtext = driver.find_element(By.CSS_SELECTOR, "div.CX6Ruf.ataLTc")
        print(Readtext.text)

    except TimeoutException:
        print("Loading took too much time!")

    driver.close()
