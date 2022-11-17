from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
# 웹 파싱
res = requests.get("https://www.dankook.ac.kr/web/kor/-550")
bs = BeautifulSoup(res.content, 'html.parser')
# print(bs)

#1페이지 제목 스크랩 테스트
title_list = bs.find_all('div',{'class' : 'subject_txt'})

for i in title_list:
    print(i.getText())