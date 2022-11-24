from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
# 크롤링 클래스 구현

# UserAgent
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

class CrawlingDku:
    menu_list = {'news': '-550', 'notice': '-390', 'today': 'dku-today'}
    # usage : url_head + menu[] + middle + page + str(pagenum)
    url_head = "https://www.dankook.ac.kr/web/kor/"
    url_middle = "?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_count=1&_Bbs_WAR_bbsportlet_orderBy=createDate&_Bbs_WAR_bbsportlet_action=view&&_Bbs_WAR_bbsportlet_curPage="
    def __init__(self, pagenum):
        self.pagenum = pagenum
        # self.url = self.url_head + self.url_page + str(pagenum)
        #웹 파싱
        # res = requests.get(self.url, headers=headers)
        # res.raise_for_status()
        # self.bs = BeautifulSoup(res.text, 'html.parser')

    def getTitle(self):
        print('------title list------')
        # 제목 스크랩
        title_list = self.bs.find_all('div', {'class': 'subject_txt'})
        for i in title_list:
            print(i.getText())
        return title_list

    def getUrl(self):
        print('------url list------')
        # 게시글 링크 스크랩
        title_link = self.bs.find_all('div', {'class': 'plus'})
        for i in title_link:
            print(i.a['href'])
        return title_link

    def getViewCount(self):
        print('------viewcount list------')
        # 게시글 조회수 스크랩
        r_view = self.bs.find_all('p', {'class': 'r_view'})
        for i in r_view:
            print(i.getText())
        return r_view

    def getDate(self):
        print('------date list------')
        # 게시글 등록일자 스크랩
        date = self.bs.find_all('p', {'class': 'date'})
        for i in date:
            print(i.getText())
        return date

    def getImgUrl(self):
        print('------img url list------')
        # 게시글 이미지 url 스크랩
        img_url = self.bs.find_all('div', {'class': 'r_img'})
        for i in img_url:
            print('https://www.dankook.ac.kr/' + i.img['src'])
        return img_url

class CrawlingNews(CrawlingDku):
    def __init__(self, pagenum):
        super().__init__(pagenum)
        self.url = CrawlingDku.url_head + CrawlingDku.menu_list['news'] + CrawlingDku.url_middle + str(self.pagenum)
        #웹 파싱
        res = requests.get(self.url, headers=headers)
        res.raise_for_status()
        self.bs = BeautifulSoup(res.text, 'html.parser')

    def getTitle(self):
        print('------title list------')
        # Dku news 페이지 제목 스크랩
        title_list = self.bs.find_all('div', {'class': 'subject_txt'})
        for i in title_list:
            print(i.getText())
        return title_list

    def getUrl(self):
        print('------url list------')
        # Dku news 게시글 링크 스크랩
        title_link = self.bs.find_all('div', {'class': 'plus'})
        for i in title_link:
            print(i.a['href'])
        return title_link

    def getViewCount(self):
        print('------viewcount list------')
        # Dku news 게시글 조회수 스크랩
        r_view = self.bs.find_all('p', {'class': 'r_view'})
        for i in r_view:
            print(i.getText())
        return r_view

    def getDate(self):
        print('------date list------')
        # Dku news 게시글 등록일자 스크랩
        date = self.bs.find_all('p', {'class': 'date'})
        for i in date:
            print(i.getText())
        return date

    def getImgUrl(self):
        print('------img url list------')
        # Dku news 게시글 이미지 url 스크랩
        img_url = self.bs.find_all('div', {'class': 'r_img'})
        for i in img_url:
            print('https://www.dankook.ac.kr/' + i.img['src'])
        return img_url

class CrawlingNotice(CrawlingDku):
    def __init__(self, pagenum):
        super().__init__(pagenum)
        self.url = CrawlingDku.url_head + CrawlingDku.menu_list['notice'] + CrawlingDku.url_middle + str(self.pagenum)
        #웹 파싱
        res = requests.get(self.url, headers=headers)
        res.raise_for_status()
        self.bs = BeautifulSoup(res.text, 'html.parser')

    def getTitle(self):
        print('------title list------')
        # Dku notice 페이지 제목 스크랩
        title_list = self.bs.find_all('div', {'class': 'subject_txt'})
        for i in title_list:
            print(i.getText())
        return title_list

    def getUrl(self):
        print('------url list------')
        # Dku notice 게시글 링크 스크랩
        title_link = self.bs.find_all('div', {'class': 'subject'})
        for i in title_link:
            print(i.a['href'])
        return title_link

    def getViewCount(self):
        print('------viewcount list------')
        # Dku notice 게시글 조회수 스크랩
        r_view = self.bs.find_all('span', {'class': 'table_hit'})
        for i in r_view:
            i.find('strong').decompose()
            print(i.getText())
        return r_view
    def getDate(self):
        print('------date list------')
        # Dku notice 게시글 등록일자 스크랩
        date = self.bs.find_all('span', {'class': 'table_date'})
        for i in date:
            i.find('strong').decompose()
            print(i.getText())
        return  date

    # def getImgUrl(self):
    #     print('------img url list------')
    #     # Dku notice 게시글 이미지 url 스크랩
    #     img_url = self.bs.find_all('div', {'class': 'r_img'})
    #     for i in img_url:
    #         print('https://www.dankook.ac.kr/' + i.img['src'])
    #     return img_url

class CrawlingToday(CrawlingDku):
    def __init__(self, pagenum):
        super().__init__(pagenum)
        self.url = CrawlingDku.url_head + CrawlingDku.menu_list['today'] + CrawlingDku.url_middle + str(self.pagenum)
        #웹 파싱
        res = requests.get(self.url, headers=headers)
        res.raise_for_status()
        self.bs = BeautifulSoup(res.text, 'html.parser')

    def getTitle(self):
        print('------title list------')
        # Dku today 페이지 제목 스크랩
        title_list = self.bs.find_all('div', {'class': 'subject_txt'})
        for i in title_list:
            print(i.getText())
        return title_list

    def getUrl(self):
        print('------url list------')
        # Dku news 게시글 링크 스크랩
        title_link = self.bs.find_all('div', {'class': 'plus'})
        for i in title_link:
            print(i.a['href'])
        return title_link

    def getViewCount(self):
        print('------viewcount list------')
        # Dku news 게시글 조회수 스크랩
        r_view = self.bs.find_all('p', {'class': 'r_view'})
        for i in r_view:
            print(i.getText())
        return r_view

    def getDate(self):
        print('------date list------')
        # Dku news 게시글 등록일자 스크랩
        date = self.bs.find_all('p', {'class': 'date'})
        for i in date:
            print(i.getText())
        return date

    def getImgUrl(self):
        print('------img url list------')
        # Dku news 게시글 이미지 url 스크랩
        img_url = self.bs.find_all('div', {'class': 'r_img'})
        for i in img_url:
            print('https://www.dankook.ac.kr/' + i.img['src'])
        return img_url


t = CrawlingNews(1)
t.getTitle()
t.getUrl()
t.getDate()
t.getViewCount()
t.getImgUrl()
