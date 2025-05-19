import requests
from bs4 import BeautifulSoup
import json
import time

# Initial page URL
URL = 'https://www.lawspot.gr/nomikes-plirofories/nomothesia/syntagma-tis-ellados'
BASE_URL = 'https://www.lawspot.gr'

# Fetch main list page
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

            # Visit each article page
            article_response = requests.get(full_url)
            article_response.encoding = 'utf-8'

            if article_response.status_code == 200:
                article_soup = BeautifulSoup(article_response.text, 'html.parser')

                # Extract title
                title_tag = article_soup.find('h1', class_='fs-28')
                title = title_tag.text.strip() if title_tag else ''

                # Extract date
                date_tag = article_soup.find('span', class_='date-display-single')
                date = date_tag.text.strip() if date_tag else ''

                # Extract article paragraphs
                content_div = article_soup.find('div', class_='law-article-content')
                paragraphs = content_div.find_all('p') if content_div else []
                content = [p.text.strip() for p in paragraphs]

                print(f"Title: {title}")
                # Append to data
                data.append({
                    'title': title,
                    'link': full_url,
                    'date': date,
                    'content': content
                })

                # Optional delay to be polite to the server
                time.sleep(1)

    # Save to JSON
    with open('laws.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("OK: Data saved to 'laws1.json'")

else:
    print(f'Failed to fetch main page. Status code: {response.status_code}')
