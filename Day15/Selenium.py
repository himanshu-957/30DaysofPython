from posixpath import join
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget

driver = webdriver.Chrome('C:/Users/Mukul/Pictures/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()
username.send_keys("himanshujadon30")
password.send_keys("******")
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder = 'Search']")))
search_box.clear()
keyword = '#dog'
search_box.send_keys(keyword)
search_box.send_keys(Keys.ENTER)
search_box.send_keys(Keys.ENTER)
driver.execute_script("window.scrollTo(0,4000);")
images = driver.find_element_by_tag_name("img")
images = [image.get_attribute('src') for image in images]
path = os.getcwd()
path = os.path.join(path, keyword[1:]+"s")
os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:]+str(counter)+'.jpg')
    wget.download(image, save_as)
    counter += 1
