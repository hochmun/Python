"""
날짜 : 2023/01/17
이름 : 심규영
내용 : 파이썬 기상청 날씨 크롤링 실습
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import pymysql

# 함수
def f(index:int, x:str):
    if x == " " : return ""
    else : return f"`col{index}` = '{x}', "

def f2(tds:list[WebElement]):
    sql = "insert into `weather` set "
    for i in range(1, 14):
        sql += f(i, tds[i-1].text)
    sql += "`rdate` = NOW()"
    return sql

# 데이터 베이스 접속
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="1234",
    db="java2db",
    charset="utf8"
)

# SQL 실행 객체
cur = conn.cursor()

# 가상 브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 페이지 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 지역명 출력
trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')

for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR, 'td')

    # SQL 실행
    cur.execute(f2(tds))

# 커밋
conn.commit()

# 프로그램 종료
conn.close()
browser.close()
print('프로그램 종료')