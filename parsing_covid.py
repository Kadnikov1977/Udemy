import requests
from bs4 import BeautifulSoup

URL = 'https://ncov.blog/countries/ru/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
           'accept': '*/*'}
response = requests.request("GET", URL, headers=HEADERS)
# print(response.text)
html_data = BeautifulSoup(response.text, 'html.parser')
quotes = html_data.find_all(class_='text-dark')
quotes1 = html_data.find_all(class_='badge badge p-2 badge-info')
new_list = [t.text for t in quotes]
new_list1 = [t.text for t in quotes1]
# print(len(new_list))
# print(len(new_list1))
text_for_print = ''
for i in range(0, len(new_list)):
    text_for_print += str(i + 1) + '.' + new_list[i] + '-' + new_list1[i] + '\n'
print(text_for_print)
# for quote in quotes:
#     print(quote.text)
# for i in range(1,j):
#     # print(f'{i}. {quotes.text[i]} - {quotes1.text[i]}')
#     print(quotes.text)

# def get_html(Url, params=None):
#     r = requests.get(Url, headers=Headers, params=params)
#     r.encoding = 'utf-8'
#     return r
#
# def parse():
#     html = get_html(Url)
#     print(html.text)
#
#
# parse()