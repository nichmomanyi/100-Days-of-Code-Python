import requests
from twilio.rest import  Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "V4T499YXU4UFIPXI"
NEWS_API_KEY = "91a92780e73b4c9fab89fc5d6fc69ffb"

# Get yesterday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
# Data dictionary to list
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_data = yesterday_data["4. close"]
print(yesterday_closing_data)

# Day before yesterday's closing stock price
dey_before_yesterday_data = data_list[1]
day_before_yesterday_closing_data = dey_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_data)

# Find the positive difference between 1 and 2
difference = abs(float(yesterday_closing_data) - float(day_before_yesterday_closing_data))
print(difference)

# The percentage difference
percentage_difference = (difference / float(yesterday_closing_data)) * 100
print(percentage_difference)

# Use the News API to get articles related to the COMPANY_NAME.
news_param = {
    "apiKey":NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
}

if percentage_difference > 1:
    news_response = requests.get(NEWS_ENDPOINT, params=news_param)
    articles = news_response.json()["articles"]
    # printing the first 3 articles
    three_articles = articles[:3]
    print(three_articles)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# A list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"Headline: {article['title']} \n Brief: {article['description']} " for article in three_articles]

# Send each article as a separate message via Twilio.
account_sid = "AC39b6ca493feb968b2f527c00fd018bca"
auth_token = "0e7c91ceafaf2f8c450d0ec01c7fe2e1"

client = Client(account_sid, auth_token)

for article in formatted_articles:
    message = client.messages.create(
        from_='+15134079698',
        to='+254715210571',
        body= article
    )
# Format the message
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
