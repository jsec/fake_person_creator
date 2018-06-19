import requests
from bs4 import BeautifulSoup


def get_page_data():
    page = requests.get('https://fakepersongenerator.com')
    if page.status_code == 200:
        return get_page_object(page)


def get_page_object(page):
    return BeautifulSoup(page.content, 'html.parser')
