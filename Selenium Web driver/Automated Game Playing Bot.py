from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(r"C:\Users\user\chromedriver", options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_click = driver.find_element(By.ID, value="cookie")
cookie_click.click()
