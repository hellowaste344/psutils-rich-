import webbrowser
import requests
from rich import print
from bs4 import BeautifulSoup 

#url = "https://en.wikipedia.org/wiki/Aaron_Swartz"
url = input("url -> ")

c = webbrowser.get('firefox')
c.open_new_tab(url)

try:
    response = requests.get(url, timeout=5)
    response.status_code
except:
    raise Exception("Couldn't fetch the url \nexiting...")

soup = BeautifulSoup(response.text, "html.parser")

data = {
    "title": soup.title.string if soup.title else None,
    "headings": [h.get_text(srip=True) for h in soup.find_all(["h1","h2","h3"])],
    "paragraphs": [p.get_text(strip=True) for p in soup.find_all(["p"])],
    "links": [a["href"] for a in soup.find_all("a",href=True)]
}


for key, value in data.items():
    print(f"\n==={key.upper()}===\n")
    for item in value if isinstance(value, list) else [value]:
        print(f"[light blue] {item}")