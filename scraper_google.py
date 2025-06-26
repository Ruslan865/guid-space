import requests
from bs4 import BeautifulSoup
import random
import time

def search(query):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)..."
    ]
    headers = {"User-Agent": random.choice(user_agents)}
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&hl=en"

    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        results = [tag.get_text() for tag in soup.select("div.BNeawe.vvjwJb.AP7Wnd")]
        if not results:
            results = [tag.get_text() for tag in soup.select("div.BNeawe.s3v9rd.AP7Wnd")]
        return results[:2] if results else ["Google nəticə tapılmadı."]
    except Exception as e:
        return [f"Google xətası: {e}"]