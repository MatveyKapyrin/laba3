import re
import requests
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup

with open('examle.html', 'r') as file:
    html_content = file.read()
    print(html_content)

# Извлекаем текст из HTML-документа
soup = BeautifulSoup(html_content, "html.parser")
text = soup.get_text()

# Используем регулярное выражение для поиска всех адресов электронной почты
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)

# Выводим найденные адреса электронной почты
for email in emails:
    print(email)


