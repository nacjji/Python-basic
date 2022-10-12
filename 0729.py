#웹크롤링 
#html 소스 가져오기
# requests.get(url)
# res.content(바이너리값)
#html 소스는 파이썬에서 의미 없음 > 파싱
# beautifulsoup 사용
# 셀렉터 표현
#태그 그대로, id#, class. , 하위태그>
# soup.select : 태그들 리스트
# soup.select_one : 태그
# .text 텍스트 부분 추출
# .get(속성명) : 속성값 추출

#웹프로그래밍 3대 언어
# html 뼈대 
# css 꾸며줌
# js 동적처리


#파일의 종류
#텍스트 파일
#바이너리 파일 #rb,wb

from bs4 import BeautifulSoup
import requests
import os

# res = requests.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4&oquery=%EC%98%81%ED%99%94&tqi=hXMwrsprvhGssU4ZF0hssssstBw-496899")
# soup = BeautifulSoup(res.text,"html.parser")   #BeautifulSoup(a,"b") # a에는 파이썬 문자열, b에는 html.parser 파이썬 문자열(html코드를)

#     # print(soup.select("a"))   #() 안의 태그를 가져옴
# for i in soup.select(".title_box > .name")[:10]:
#     print(i.text) #.class=("요거") 해당 태그 하나 가져오기 # or span.title

# res = requests.get(f"https://kitribob.wiki/images/f/f9/%ED%95%B5%EA%B7%80%EC%9A%A4.png")
# f=open("hansam.png","wb")
# f.write(res.content)

# st = """
# <html id="a">
#     <body class="b">
#         <div id="hello1" here="jeju1">안녕1</div>
#         <div class="hello2" here="jeju2">안녕2</div>
#         <div id="c">
#             <span class="d" here="jeju3">안녕3</span>
#         </div>
#         <span>안녕4</span>
#         <a href="https://www.naver.com">NAVER로가기</a>
#     </body>
# </html>
# """
# soup = BeautifulSoup(st,"html.parser")
# print(soup.select_one("#hello1").get("here"))
# print(soup.select_one(".hello2").get("here"))
# print(soup.select_one(".d").get("here"))
# print(soup.select_one("#a").get("href"))
# .get(속성명) : 속성값 추출


# os.mkdir()   #폴더만드는 함수


# def 폴더생성(st):
#     if os.path.isdir(st):
#         pass
#     else:
#         os.mkdir(st)

# def 제거(st):
#     for i in ":?*<>|\/\"":
#         st = st.replace(i, "")
#     return st

# 폴더생성("웹툰")

# for k in ["mon","tue","wed","thu","fri","sat","sun"]:
#     폴더생성(f"웹툰/{k}")
#     res = requests.get(f"https://comic.naver.com/webtoon/weekdayList?week={k}")
#     soup = BeautifulSoup(res.text, "html.parser")

#     for i in soup.select(".thumb > a > img")   :
#         웹툰제목 = i.get("title")
#         링크 = i.get("src")
#         r = requests.get(링크)
#         f = open(f"웹툰/{k}/{제거(웹툰제목)}.png", "wb")
#         f.write(r.content)

from bs4 import BeautifulSoup

# st = """<html>
#     <body>
#         <div id="champ">
#             <span class="name">KENNEN</span>
#             <span class="hp">600</span>
#             <span class="mp">0</span>
#         </div>
#         <div id="champ">
#             <span class="name">TEEMO</span>
#             <span class="hp">400</span>
#             <span class="mp">400</span>
#         </div>
#         <div id="champ">
#             <span class="name">VEIGAR</span>
#             <span class="hp">300</span>
#             <span class="mp">500</span>
#         </div>
#     </body>
# </html>"""

# soup = BeautifulSoup(st, "html.parser")


# for i in soup.select("#champ"):
#     print(i.select_one(".name").text)
#     print(i.select_one(".hp").text)
#     print(i.select_one(".mp").text) 
#     print()

def 폴더생성(st):
    if os.path.isdir(st):
        pass
    else:
        os.mkdir(st)





res = requests.get(f"https://lol.inven.co.kr/dataninfo/champion/")
soup = BeautifulSoup(res.text, "html.parser")
# print(soup.select(".champName"))
# for i in soup.select(".champListUL > #li"):
#     print(i.select_one("#img"))
#     print(i.select_one("#nobr").text)

    # f=open("lolinven/")

def 걸러(st):
    for i in ":?*<>|\/\"":
        st = st.replace(i,"")
    return st

폴더생성("lolinven")
for i in soup.select(".champImage > a"):
    이름 = i.get("title")
    링크 = "https:"+i.select_one("img").get("src")
    r = requests.get(링크)
    f = open(f"lolinven/{걸러(이름)}.png","wb")
    f.write(r.content)



#주말과제! 
#포켓몬고 인벤에서 포켓몬 저장하기
# https://pokemongo.inven.co.kr/dataninfo/pokemon/