from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(r"C:\Users\user\chromedriver", options=chrome_options)


driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_driver = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(f"There are: {article_driver.text} ")