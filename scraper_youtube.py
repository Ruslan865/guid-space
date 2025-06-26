import requests
from bs4 import BeautifulSoup

def search(query):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        # Video ID-ləri javascript vasitəsilə yükləndiyindən ilk nəticəni süzgəcdən keçiririk
        for script in soup.find_all("script"):
            if "videoRenderer" in script.text:
                start = script.text.find("videoId")
                if start != -1:
                    video_id = script.text[start+10:start+21]
                    return [f"https://www.youtube.com/watch?v={video_id}"]
        return ["YouTube nəticəsi tapılmadı."]
    except Exception as e:
        return [f"YouTube xətası: {e}"]