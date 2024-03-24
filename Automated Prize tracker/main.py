import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/dp/B0BP9MDCQZ/ref=va_live_carousel?pf_rd_r=2N9QDCJMDJ52Q4R4583P&pf_rd_p=38e95550-e353-4631-82b6-9e1a1bda0585&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=HighVelocityEvent&pf_rd_i=deals_1_desktop&pf_rd_s=slot-13&pd_rd_w=pZnKz&pd_rd_r=e89dc738-54ba-41d1-8072-cf4af48f7c19&pd_rd_wg=teGrL&asc_contentid=amzn1.amazonlive.broadcast.aa58fc6b-d695-4ea2-aa33-f7a7371dae11&pd_rd_i=B0BP9MDCQZ&th=1&psc=1"

ACCEPT_LANGUAGE = "en-GB,en-US;q=0.9,en;q=0.8"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

headers = {
    "Accept-Language":ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-price-whole").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


my_email = "nmomce44@gmail.com"
password = "vntfgxmruewsfcqy"

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 15

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="nicholasmomanyi94@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
