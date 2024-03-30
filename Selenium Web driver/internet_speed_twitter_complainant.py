from selenium import webdriver
import selenium

PROMISED_UP = 5
PROMISED_DOWN = 10
TWITTER_EMAIL = "nmomce44@gmail.com"
TWITTER_PASS = "nichdee254"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(r"C:\Users\user\chromedriver", options=chrome_options)

driver.get("")