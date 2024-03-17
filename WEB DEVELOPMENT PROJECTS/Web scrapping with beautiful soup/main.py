from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "lxml")

anchor_tags = soup.find_all(name="p")
for tag in anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

heading = soup.find(name= "h1", id="name" )
print(heading)

company_url = soup.select_one("p a")
print(company_url)

