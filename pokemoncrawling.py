import os
from bs4 import BeautifulSoup
import requests




def 폴더생성(st):
    if os.path.isdir(st):
        pass
    else:
        os.mkdir(st)

res = requests.get("https://pokemongo.inven.co.kr/dataninfo/pokemon/")
soup = BeautifulSoup(res.text,"html.parser")


def 걸러(st):
    for i in ":?*<>|\/\"":
        st = st.replace(i,"")
    return st


폴더생성("pokemon")
for i in soup.select(".pokemonicon"):
    이름 = i.select_one(".pokemonname").text
    이미지 = "https:"+i.select_one("a>img").get("src")
    f=open(f"pokemon/{걸러(이름)}.png","wb")
    r=requests.get(이미지)
    f.write(r.content)
