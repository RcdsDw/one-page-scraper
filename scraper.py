import requests
import csv
import json
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://methodwakfu.com/pvm/les-archimonstres/')
headers=headers

soup = BeautifulSoup(page.text, 'html.parser')

trs = soup.find_all('tr')

tab = []

for tr in trs:
    name = tr.find('td', class_="column-1")
    lvl = tr.find('td', class_="column-3")
    timer = tr.find('td', class_="column-4")
    location = tr.find('td', class_="column-5")

    if name and lvl and timer and location:
        tab.append({
            'title': name.get_text(strip=True),
            'lvl': lvl.get_text(strip=True),
            'timer': timer.get_text(strip=True),
            'location': location.get_text(strip=True)     
        })

# results on console
for t in tab:
    print(' \n', t)

# results in a csv file
with open('res.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['title', 'lvl', 'timer', 'location'])
    for t in tab:
        writer.writerow(t.values())

# results in a json file
with open('res.json', 'w', encoding='utf-8') as json_file:
    json.dump(tab, json_file, ensure_ascii=False, indent=2)