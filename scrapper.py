from bs4 import BeautifulSoup
import requests

base_url = "https://myanimelist.net/topmanga.php?limit="
total_mangas = 0
for i in range(0, 250, 50):
    url = base_url + str(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    items = soup.find_all(class_='ranking-list')

    for item in items:
        title = item.find(class_="manga_h3").text.strip()
        src = item.find('img').get('data-src')
        detail = item.find(class_="information di-ib mt4").text.strip()
        print("----------------------------------------------------")
        print(f"TITLE: {title}")
        print(f"SRC: {src}")
        print(f"Detail: {detail}")
        print("-----------------------------------------------------")
        total_mangas += 1


print(f"TOTAL: {total_mangas}")
