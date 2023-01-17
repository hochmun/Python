"""
날짜 : 2023/01/16
이름 : 심규영
내용 : 파이썬 네이버 뉴스 크롤링 실습
"""
import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook
import sys

date = 0

print('날짜를 입력하세요')
print('ex)20230101, -없이 년월일 입력')

try:
    date = int(input())
except:
    print('숫자를 입력하십시오.')
    print('프로그램 종료')
    sys.exit()

pg = 1
count = 1
workbook = Workbook()

sheet = workbook.active

sheet.append(['날짜','페이지','뉴스 번호','제목','링크'])

while True :
    # HTML 요청
    url = f'https://news.naver.com/main/list.naver?mode=LS2D&sid2=230&sid1=105&mid=shm&date={date}&page={pg}'
    html = req.get(url, headers={'User-Agent':'Mozilla/5.0'}).text

    # 문서 객체 생성
    dom = bs(html, 'html.parser')

    currentPage = dom.select_one("#main_content > div.paging > strong").text
    if str(pg) != currentPage:
        break

    # 데이터 파싱
    lis = dom.select('#main_content > div.list_body.newsflash_body > ul > li')

    for li in lis:
        tag_a = li.select_one('dl > dt:not(.photo) > a')
        title = tag_a.text
        href = tag_a['href']

        sheet.append([date,pg,count,title,href])

        count += 1

    pg += 1

workbook.save('C:/Users/java2/Desktop/news.xlsx')
workbook.close()

print('프로그램 종료')