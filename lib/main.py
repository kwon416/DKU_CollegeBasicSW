from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
# 크롤링 클래스 구현

# UserAgent
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

def crawling(key, pagenum):
    url_head= "https://www.dankook.ac.kr/web/kor/-550?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_count=1&_Bbs_WAR_bbsportlet_orderBy=createDate&_Bbs_WAR_bbsportlet_action=view"
    url_page = "&_Bbs_WAR_bbsportlet_curPage="

    url = url_head + url_page + str(pagenum)

    # 웹 파싱
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    bs = BeautifulSoup(res.text, 'html.parser')

    #제목 스크랩
    title_list = bs.find_all('div',{'class' : 'subject_txt'})
    print(title_list)
    for i in title_list:
        print(i.getText())

    #게시글 링크 스크랩
    title_link = bs.find_all('div',{'class':'plus'})
    for i in title_link:
        print(i.a['href'])

    #게시글 조회수 스크랩
    r_view = bs.find_all('p', {'class':'r_view'})
    for i in r_view:
        print(i.getText())

    # 게시글 등록일자 스크랩
    date = bs.find_all('p', {'class': 'date'})
    for i in date:
        print(i.getText())

    #게시글 이미지 url 스크랩
    img_url = bs.find_all('div', {'class': 'r_img'})
    for i in img_url:
        print('https://www.dankook.ac.kr/' + i.img['src'])


crawling('', 1)