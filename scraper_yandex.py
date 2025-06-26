import requests
from bs4 import BeautifulSoup

def search(query):
    try:
        url = f"https://yandex.com/search/?text={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        results = [tag.get_text() for tag in soup.select("li.serp-item")]
        return results[:1] if results else ["Yandex nəticəsi tapılmadı."]
    except Exception as e:
        return [f"Yandex xətası: {e}"]