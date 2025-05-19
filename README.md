# Web Scraper for Greek Constitution Articles

This project is a Python-based web scraper designed to extract articles from the Greek Constitution - Syntagma hosted on [Lawspot.gr](https://www.lawspot.gr). It collects article titles, publication dates, and full article content, then saves the data as a structured JSON file.

---

## Features

* Scrapes a main page listing Constitution articles
* Follows each article link to retrieve detailed content
* Extracts article title, date, and full text paragraphs
* Saves all scraped data into a UTF-8 encoded JSON file (`laws.json`)
* Simple, easy-to-read Python code using `requests` and `BeautifulSoup`
* Includes polite delay between requests to avoid overwhelming the server

---

## Requirements

* Python 3.7 or higher
* [requests](https://pypi.org/project/requests/)
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)


## Notes

* This scraper is intended for educational and personal use.
* Please respect website terms of service and scraping policies.
* Consider adding error handling and support for pagination if needed.

---

## License

This project is licensed under the MIT License.
