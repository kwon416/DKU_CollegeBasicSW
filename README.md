# DKU_CollegeBasicSW
단국대학교 대학기초SW입문 팀 프로젝트 저장소입니다.

참고자료
https://wikidocs.net/35482 ㅡ Qt Designer를 이용한 UI의 제작과 연결

## 프로젝트 개요
단국대 홈페이지에서 DKU NEWS, DKU NOTICE, DKU TODAY 정보를 스크래핑하여 Python GUI를 활용해 단국대학교의 소식을 모아 볼 수 있는 프로그램 제작.

크롤링 내용: 게시글title + 본문 링크 url + 작성일자 + 조회수 + 게시글 타이틀 이미지

PyQT GUI로 크롤링 내용 출력

## 사용 tool & Library
개발 언어: Python 3.10

IDE 환경:  Pycharm

웹 파싱 & 크롤링: requests, beautifulsoup4

사용자 GUI: pyQt5, QtUtil

웹 리소스 가져오기: urllib, webbrowser

etc: ssl

## 클래스 구성설명
크롤링 상위 클래스 : CrawlingDku

크롤링 하위 클래스 : CrawlingNews, CrawlingNotice, CrawlingToday

GUI 최상위 클래스 : QDialog

GUI 하위 UI 클래스 : HomeUI, ArticleUI

ArticleUI 하위 클래스 : NewsUI, TodayUI, NoticeUI

