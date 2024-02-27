import re
import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# print(soup)

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# # print(quotes)
# print(authors)

# # for quote in quotes:
# #     print(quote.text)
# for  author in authors:
#     print(author.text)

tags = soup.find_all("div", class_="tags")
# print(tags)
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(f"--{authors[i].text}")
    tagsforquote = tags[i].find_all("a", class_="tag")
    for tagforquote in tagsforquote:
        print(tagforquote.text)
    break # exit after first quotes if you want all comment break


if __name__ == '__main__':
    pass
    # result = main(get_urls())
