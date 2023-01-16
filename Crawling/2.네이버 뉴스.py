"""
날짜 : 2023/01/16
이름 : 심규영
내용 : 파이썬 네이버 뉴스 크롤링 실습
"""
import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook

pg = 1
count = 1
#lis2 = []
workbook = Workbook()

sheet = workbook.active

sheet.append(['페이지','뉴스 번호','제목','링크'])

while True :
    # HTML 요청
    url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=230&sid1=105&mid=shm&date=20230116&page=%d' % pg

    html = req.get(url, headers={'User-Agent':'Mozilla/5.0'}).text
    #print(html)

    # 문서 객체 생성
    dom = bs(html, 'html.parser')

    currentPage = dom.select_one("#main_content > div.paging > strong").text

    if str(pg) != currentPage:
        break

    # 데이터 파싱
    #tit = dom.select_one('#main_content > div.list_header.newsflash_header > h3').text
    #print('tit :', tit)

    lis = dom.select('#main_content > div.list_body.newsflash_body > ul > li')
    #if lis2 == lis:break
    #else: lis2 = lis

    for li in lis:
        tag_a = li.select_one('dl > dt:not(.photo) > a')
        title = tag_a.text
        href = tag_a['href']

        sheet.append([pg,count,title,href])

        #print('count :', count)
        #print('title :', title.strip())
        #print('href :', href)
        count += 1

    pg += 1

workbook.save('C:/Users/java2/Desktop/news.xlsx')
workbook.close()

print('프로그램 종료')