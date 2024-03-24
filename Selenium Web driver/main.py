from selenium import webdriver
from selenium.webdriver.common.by import By



# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(r"C:\Users\user\chromedriver", options=chrome_options)


# driver.get("https://www.kilimall.co.ke/listing/19436181?sku_id=19436181&image=https://image.kilimall.com/kenya/shop/store/goods/9480/2024/01/1705372136568420d542bfccf4229bf86cb38b5510cd8_360.jpg.webp%23&title=Fashion+Square+LED+Digital+Watch+Students+Luminous+Electroplated+sports+Electronic+Watch+Wrist+Watch+For+Men+And+Women+BlackBlack&from=flash-sale&source=")
#
# price_kes = driver.find_element(By.CLASS_NAME, value="sale-price").text
# print(f" The price is {price_kes}")

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name":event_names[n].text
    }
print(events)



# driver.close()
# driver.quit()
