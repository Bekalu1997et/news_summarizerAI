import requests
from bs4 import BeautifulSoup

def scrape_article(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    article = "\n".join(paragraphs)
    return article.strip()