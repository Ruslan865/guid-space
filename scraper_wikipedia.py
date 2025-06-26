import wikipedia
from bs4 import BeautifulSoup

def detect_language(query):
    # Azərbaycan dilinə aid hərflər varsa, 'az' seç
    az_chars = "əıöüğçş"
    tr_chars = "ıöüğçş"
    if any(char in query.lower() for char in az_chars):
        return "az"
    elif any(char in query.lower() for char in tr_chars):
        return "tr"
    else:
        return "en"

def search(query):
    for lang in [detect_language(query), "tr", "en"]:
        wikipedia.set_lang(lang)
        try:
            results = wikipedia.search(query)
            if not results:
                continue  # Növbəti dilə keç
            page = wikipedia.page(results[0], auto_suggest=False)
            html = page.html()
            soup = BeautifulSoup(html, features="html.parser")
            text = soup.get_text()
            return [text[:500]]
        except Exception:
            continue  # Xəta olsa belə növbəti dili yoxla
    return [f"Wikipedia nəticəsi tapılmadı: {query}"]