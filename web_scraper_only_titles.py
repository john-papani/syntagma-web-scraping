import requests
from bs4 import BeautifulSoup
import json

# URL to scrape
URL = 'https://www.lawspot.gr/nomikes-plirofories/nomothesia/syntagma-tis-ellados'  # replace with your target URL



# Base URL for constructing full links
BASE_URL = 'https://www.lawspot.gr'

## Fetch the page
response = requests.get(URL)
response.encoding = 'utf-8'

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select('.law-article.box')

    data = []
    for article in articles:
        link_tag = article.find('a', class_='title')
        if link_tag:
            href = link_tag.get('href')
            full_url = BASE_URL + href
            title_tag = link_tag.find('h4')
            title = title_tag.text.strip() if title_tag else ''
            data.append({
                'title': title,
                'link': full_url
            })

 # Save to JSON file
    with open('laws.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("OK: Data saved to 'laws.json'")
else:
    print(f'Failed to fetch the page. Status code: {response.status_code}')