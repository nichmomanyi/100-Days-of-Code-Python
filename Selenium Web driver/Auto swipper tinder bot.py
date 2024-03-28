from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(r"C:\Users\user\chromedriver", options=chrome_options)
driver.get("https://tinder.com/")

sleep(2)
log_in = driver.find_element(By.LINK_TEXT, value="Log in")
log_in.click()

sleep(2)
gm_login = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[2]')
gm_login.click()