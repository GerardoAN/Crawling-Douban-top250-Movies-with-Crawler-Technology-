import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"}

content = requests.get("https://movie.douban.com/top250", headers=headers)
html = content.text

soup = BeautifulSoup(html, "html.parser")

for start_num in range(0, 250, 25):
    content = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    html = content.text
    soup = BeautifulSoup(html, "html.parser")
    all = soup.find_all("div", attrs={"class": "hd"})
    for i in all:
        # # name=i.find("span")
        # # print(name)
        # print(i)
        name = i.find_all("span", attrs={"class": "title"})
        for j in name:
            # print(j.string)
            if "/" not in j.string:
                print(j.string)
