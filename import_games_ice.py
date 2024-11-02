from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Specify the path to your Edge WebDriver
driver_path = r'edgedriver_win64\msedgedriver.exe'
service = EdgeService(driver_path)
driver = webdriver.Edge(service=service)

driver.get("https://www.ice.hockey/en/schedule/schedule")

wait = WebDriverWait(driver, 10)

try:
    shadow_host = wait.until(EC.presence_of_element_located((By.ID, "cmpwrapper")))
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    accept_button = shadow_root.find_element(By.CSS_SELECTOR, "a.cmpboxbtn.cmpboxbtnyes")
    accept_button.click()
    print("Cookies accepted.")
except Exception as e:
    print("No cookie consent button found or unable to accept cookies.")

time.sleep(5)



