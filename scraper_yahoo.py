import requests
from bs4 import BeautifulSoup

def search(query):
    try:
        url = f"https://search.yahoo.com/search?p={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        results = [tag.get_text() for tag in soup.select("div.dd.algo.algo-sr")]
        return results[:1] if results else ["Yahoo nəticəsi tapılmadı."]
    except Exception as e:
        return [f"Yahoo xətası: {e}"]