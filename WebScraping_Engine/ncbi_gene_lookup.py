import requests
from bs4 import BeautifulSoup


def load_url(url: str):
    return requests.get(url)


def read_gene_from_url(page):
    soup_data = BeautifulSoup(page.content, 'html.parser')
    return soup_data


page = load_url('https://www.ncbi.nlm.nih.gov/nuccore/NC_045512')
for element in read_gene_from_url(page).find_all(text=True):
    print(element)
print()
