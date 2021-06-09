from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.daft.ie/"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')