from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(r"C:\Users\user\chromedriver", options=chrome_options)


driver.get("https://secure-retreat-92358.herokuapp.com/")

# article_driver = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # print(f"There are: {article_driver.text} articles")
# article_driver.click()
#
# link_clicker = driver.find_element(By.LINK_TEXT, value="Site traffic statistics")
# link_clicker.click()

# # Find the "Search <input> by Name
# search = driver.find_element(By.NAME, value="search")
#
# # Sending keyboard input to selenium
# search.send_keys("Machine learning", Keys.ENTER)
f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Nicholas", Keys.ENTER)
l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Momce", Keys.ENTER)
email = driver.find_element(By.NAME, value="email")
email.send_keys("nich@123.com", Keys.ENTER)
sign_up = driver.find_element(By.LINK_TEXT, value="Sign Up")
sign_up.click()
