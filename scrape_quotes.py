import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "http://quotes.toscrape.com"

def scrape_quotes(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []
    
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        quotes.append({
            "quote": text,
            "author": author,
            "tags": tags
        })
    return quotes

def scrape_authors(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    authors = []
    
    for author in soup.find_all('small', class_='author'):
        author_url = BASE_URL + author.find_next('a')['href']
        author_response = requests.get(author_url)
        author_soup = BeautifulSoup(author_response.text, 'html.parser')
        
        name = author_soup.find('h3', class_='author-title').text.strip()
        born_date = author_soup.find('span', class_='author-born-date').text.strip()
        born_location = author_soup.find('span', class_='author-born-location').text.strip()
        description = author_soup.find('div', class_='author-description').text.strip()
        
        authors.append({
            "fullname": name,
            "born_date": born_date,
            "born_location": born_location,
            "description": description
        })
    return authors

all_quotes = []
all_authors = []
page_number = 1

while True:
    page_url = f"{BASE_URL}/page/{page_number}/"
    response = requests.get(page_url)
    
    if "No quotes found!" in response.text:
        break
    
    all_quotes.extend(scrape_quotes(page_url))
    all_authors.extend(scrape_authors(page_url))
    
    page_number += 1

with open('quotes.json', 'w') as f:
    json.dump(all_quotes, f, indent=4)

with open('authors.json', 'w') as f:
    json.dump(all_authors, f, indent=4)
