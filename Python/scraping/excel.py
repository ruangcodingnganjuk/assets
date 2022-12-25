from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

import time

from openpyxl import load_workbook

wb = load_workbook(filename = 'namee.xlsx')

sheetRange = wb['Sheet1']

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://forms.gle/mzPyztFmtQDcaVhG9")
time.sleep(2)

#looping mode

i = 2

while i <= len(sheetRange['A']):
    nis = sheetRange['A'+str(i)].value
    nama = sheetRange['B'+str(i)].value
    matematika = sheetRange['C'+str(i)].value
    biologi = sheetRange['D'+str(i)].value
    fisika = sheetRange['E'+str(i)].value

    try:
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nis)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nama)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(matematika)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(biologi)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(fisika)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

    except TimeoutException:
        print("not found")
        pass

    time.sleep(1)
    i = i + 1

print('Done')