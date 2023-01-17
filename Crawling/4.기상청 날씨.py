"""
날짜 : 2023/01/17
이름 : 심규영
내용 : 파이썬 기상청 날씨 크롤링 실습
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pymysql

# 함수
def f(index, x:str):
    if x == " ":return
    else : return f"`col{index}` = '{x}', "


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

    sql = "insert into `weather` set "
    sql += f(1, tds[0].text)
    sql += f(2, tds[1].text)
    sql += f(3, tds[2].text)
    sql += f(4, tds[3].text)
    sql += f(5, tds[4].text)
    sql += f(6, tds[5].text)
    sql += f(7, tds[6].text)
    sql += f(8, tds[7].text)
    sql += f(9, tds[8].text)
    sql += f(10, tds[9].text)
    sql += f(11, tds[10].text)
    sql += f(12, tds[11].text)
    sql += f(13, tds[12].text)
    sql += f(14, tds[13].text)
    #sql += f"`col1` = '{tds[0].text}',"
    #sql += f"`col2` = '{tds[1].text}',"
    #sql += f"`col3` = '{tds[2].text}',"
    #if tds[3].text != " ": sql += f"`col4` = '{tds[3].text}',"
    #if tds[4].text != " ": sql += f"`col5` = '{tds[4].text}',"
    #if tds[5].text != " ": sql += f"`col6` = '{tds[5].text}',"
    #if tds[6].text != " ": sql += f"`col7` = '{tds[6].text}',"
    #if tds[7].text != " ": sql += f"`col8` = '{tds[7].text}',"
    #if tds[8].text != " ": sql += f"`col9` = '{tds[8].text}',"
    #if tds[9].text != " ": sql += f"`col10` = '{tds[9].text}',"
    #if tds[10].text != " ": sql += f"`col11` = '{tds[10].text}',"
    #sql += f"`col12` = '{tds[11].text}',"
    #if tds[11].text != " ": sql += f"`col13` = '{tds[12].text}',"
    #if tds[12].text != " ": sql += f"`col14` = '{tds[13].text}',"
    sql += "`rdate` = NOW()"

    # SQL 실행
    cur.execute(sql)

# 커밋
conn.commit()

# 프로그램 종료
conn.close()
browser.close()
print('프로그램 종료')