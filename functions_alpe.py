from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# wait = WebDriverWait(driver, 10)
def get_game_info(driver):
    wait = WebDriverWait(driver, 10)
    #Get the date
    sel_date = "#los_game > div > div > div.-hd-los-game-full-report-game-facts > div.-hd-los-game-full-report-game-fact-row.-hd-los-game-full-report-game-fact-row-scheduledDate > div.-hd-los-game-full-report-game-fact-value"
    date = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, sel_date))).text

    #Get the place
    sel_place = "#los_game > div > div > div.-hd-los-game-full-report-game-facts > div.-hd-los-game-full-report-game-fact-row.-hd-los-game-full-report-game-fact-row-location > div.-hd-los-game-full-report-game-fact-value"
    place = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, sel_place))).text

    #Get the refs
    sel_ref1 = "#los_game > div > div > div.-hd-los-game-full-report-game-facts > div.-hd-los-game-full-report-game-fact-row.-hd-los-game-full-report-game-fact-row-referee1 > div.-hd-los-game-full-report-game-fact-value"
    ref1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, sel_ref1))).text
    sel_ref2 = "#los_game > div > div > div.-hd-los-game-full-report-game-facts > div.-hd-los-game-full-report-game-fact-row.-hd-los-game-full-report-game-fact-row-referee2 > div.-hd-los-game-full-report-game-fact-value"
    ref2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, sel_ref2))).text
    sel_lin1 = "#los_game > div > div > div.-hd-los-game-full-report-game-facts > div.-hd-los-game-full-report-game-fact-row.-hd-los-game-full-report-game-fact-row-linesman1 > div.-hd-los-game-full-report-game-fact-value"
    lin1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, sel_lin1))).text
    sel_lin2 = "#los_game > div > div > div.-hd-los-game-full-report-game-facts > div.-hd-los-game-full-report-game-fact-row.-hd-los-game-full-report-game-fact-row-linesman2 > div.-hd-los-game-full-report-game-fact-value"
    lin2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, sel_lin2))).text
    sodniki = [ref1, ref2, lin1, lin2]
    print(sodniki)

    #Get the penalties info
    sel_pim = "#los_game > div > div > div.-hd-los-game-full-report-container.-hd-los-game-full-report-penalties > div.-hd-los-game-full-report-container-data.-hd-los-game-full-report-penalties-data.-hd-util-intellitable > div.-hd-util-intellitable-data > table > tbody  td:nth-child(6)"
    pim_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, sel_pim)))
    pim = [element.text for element in pim_elements]
    #print(pim) 
  
    sel_offenc = "#los_game > div > div > div.-hd-los-game-full-report-container.-hd-los-game-full-report-penalties > div.-hd-los-game-full-report-container-data.-hd-los-game-full-report-penalties-data.-hd-util-intellitable > div.-hd-util-intellitable-data > table > tbody> tr > td:nth-child(7)"
    offenc_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, sel_offenc)))
    offenc = [element.text for element in offenc_elements]
    #print(offenc)
    kategorija = "AHL"
    return sodniki, kategorija, place, date, pim , offenc

