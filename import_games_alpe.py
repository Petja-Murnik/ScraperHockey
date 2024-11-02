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

from functions_alpe import get_game_info

# Specify the path to your Edge WebDriver
driver_path = r'edgedriver_win64\msedgedriver.exe'
service = EdgeService(driver_path)
driver = webdriver.Edge(service=service)

driver.get("https://www.alps.hockey/en/home-en/season/games")


wait = WebDriverWait(driver, 10)

try:
    shadow_host = wait.until(EC.presence_of_element_located((By.ID, "cmpwrapper")))
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    accept_button = shadow_root.find_element(By.CSS_SELECTOR, "a.cmpboxbtn.cmpboxbtnyes")
    accept_button.click()
    print("Cookies accepted.")
except Exception as e:
    print("No cookie consent button found or unable to accept cookies.")


# Locate and select the first dropdown (Season 2024/25)
season_select_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#los_schedule > form > select:nth-child(1)")))
season_select = Select(season_select_element)
season_select.select_by_value("2024/25")

# Locate and select the second dropdown (preliminary round = Value 15886, else has to be changed when it starts)
league_select_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#los_schedule > form > select:nth-child(2)")))
league_select = Select(league_select_element)
league_select.select_by_value("15886")


#Click the second button that is for what time period I click it. 
#As of right now it is just one clickable such button later it will have to be a for loop or sth
second_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#los_schedule > form > div > div > button.btn.btn-secondary.active")))
second_button.click()

#Find all rows for the chosen stuff (that is one row is one game)
wait = WebDriverWait(driver, 10)
rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#los_schedule > div > div > div > div.-hd-util-intellitable-data > table > tbody tr")))

df = pd.DataFrame(columns=['date', 'kategorija','kraj', 'sodniki','dolzine kazni','vrste_kazni','link'])
for i in range(len(rows)):  # Limit to the first 2 games for testing
    try:
        # Re-fetch rows each time to avoid stale references
        rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#los_schedule > div > div > div > div.-hd-util-intellitable-data > table > tbody tr")))
        row = rows[i] 

        # Scroll to the row and click it
        driver.execute_script("arguments[0].scrollIntoView();", row)
        time.sleep(0.1) 
        # Attempt JavaScript click
        driver.execute_script("arguments[0].click();", row)
        
        #Get data and write it 
        game_link = driver.current_url
        sodniki, kategorija, place, date, pim , offenc = get_game_info(driver)
        new_row = pd.DataFrame([{
            'date': date,
            'kategorija': kategorija,
            'kraj': place,
            'sodniki': sodniki,
            'dolzine kazni': pim,
            'vrste_kazni': offenc,
            'link': game_link
        }])
        df = pd.concat([df, new_row], ignore_index=True)

        driver.back() 
    except Exception as e:
        print(f"Error accessing game {i+1}: {e}")
        break

#Write the data into a .csv
df.to_csv('rezultati_alpe.csv', index=False, encoding='utf-8')

time.sleep(5)
driver.quit()