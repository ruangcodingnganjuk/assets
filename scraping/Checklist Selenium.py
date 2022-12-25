from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe9hZ30RMpmtnJzHJRGfsIz3CJpvCHg9hUhzCrr0vYSzVeZRQ/viewform?usp=sharing")
driver.maximize_window()
time.sleep(2)

class DemoCheckboxes():
    def demo_checkbox(self):
        driver.find_element(By.XPATH, '//*[@id="i6"]/div[2]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="i12"]/div[2]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="i15"]/div[2]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="i21"]/div[2]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span').click()
        
        
checkbox = DemoCheckboxes()
checkbox.demo_checkbox()


