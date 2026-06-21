from textwrap import indent
import json
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
for quote_tag, author_tag in zip(quotes, authors):
    print(quote_tag.text)
    print(author_tag.text)

data = []
for quote_tag, author_tag in zip(quotes, authors):
    data.append({"quote": quote_tag.text, "author": author_tag.text})

with open("quotes.json", "w") as f:
    json.dump(data, f, indent=4)

print("data saved to quotes.json")

print("Albert Einstein's Quotes ")
for quote in data:
    if quote["author"] == "Albert Einstein":
        print(quote["quote"])
