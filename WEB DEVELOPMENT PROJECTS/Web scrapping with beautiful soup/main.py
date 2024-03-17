from bs4 import  BeautifulSoup
import lxml

with open("website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "lxml")
print(soup.title)
print(soup.title.name)
print(soup.a)
print(soup.p)