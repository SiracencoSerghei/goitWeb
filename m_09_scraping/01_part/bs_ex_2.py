import requests
from requests import Session
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"

with Session() as session:
    response = session.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")


# знайти перший тег <p> на сторінці
first_paragraph = soup.find("p")
# print(first_paragraph)

# знайти всі теги <p> на сторінці
all_paragraphs = soup.find_all("p")
# print(all_paragraphs)

# отримати текст першого тега <p> на сторінці
first_paragraph_text = first_paragraph.get_text()
# print(first_paragraph_text.strip())  # 'Login'

# отримати значення атрибута "href" першого тегу <a> на сторінці
first_link = soup.find("a")
first_link_href = first_link["href"]
# print(first_link_href)  # '/'

# всі дочірні елементи першого тегу <p> на сторінці
body_children = list(first_paragraph.children)
# print(body_children)

# знайти перший тег <a> всередині першого тегу <div> на сторінці
first_div = soup.find("div")
first_div_link = first_div.find("a")
# print(first_div_link)

#  батьківський елемент першого тегу <p> на сторінці
first_paragraph_parent = first_paragraph.parent
# print(first_paragraph_parent)

# методи find_parent і find_parents
# для пошуку батьківських елементів:
container = soup.find("div", attrs={"class": "quote"}).find_parent("div", class_="col-md-8")
# print(container)

#  наступний сусідній елемент першого тегу <span> з класом "tag-item" на сторінці:
next_sibling = soup.find("span", attrs={"class": "tag-item"}).find_next_sibling("span")
# print(next_sibling)

#  попередній сусідній елемент першого тегу <span> з класом "tag-item" на сторінці:
previous_sibling = next_sibling.find_previous_sibling("span")
# print(previous_sibling)

# Знайдемо всі теги <p> на сторінці
p = soup.select("p")
# print(p)

# Знайдемо всі елементи з класом "text"
text = soup.select(".text")
# print(text)

# Знайдемо всі елементи з ідентифікатором "header"
header = soup.select("#header")
# print(header)

# знайдемо всі елементи <a> всередині тегу <div> з класом "container":
a = soup.select("div.container a")
# print(a)


print(soup.find('div', class_='tags').find('a'))

if __name__ == '__main__':
    pass
    # result = main(get_urls())
    # print(result)
    # print(result := main(get_urls()))
