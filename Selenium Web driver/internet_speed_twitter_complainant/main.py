from selenium import webdriver
import selenium

PROMISED_UP = 5
PROMISED_DOWN = 10
TWITTER_EMAIL = "nmomce44@gmail.com"
TWITTER_PASS = "nichdee254"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\Users\user\chromedriver", options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot
bot.get_internet_speed()
bot.tweet_at_provider()
