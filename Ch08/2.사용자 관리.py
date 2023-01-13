"""
날짜 : 2023/01/13
이름 : 심규영
내용 : 파이썬 사용자 관리 프로그램 실습
"""
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host="127.0.0.1", 
                        user="root", 
                        passwd="1234", 
                        db="java2db", 
                        charset="utf8")
cur = conn.cursor()

while True:
    print('0: 종료, 1:등록, 2:조회, 3:검색, 4:삭제')
    answer = 0

    try:
        answer = int(input('선택 : '))
    except:
        print('숫자를 입력하세요.')
        continue

    if answer == 0:
        break
    
    elif answer == 1:
        try:
            print('아이디 이름 휴대폰 나이를 빈칸 단위로 입력하시오')
            uid, name, hp, age = map(str, input().split())
            sql = "insert into `user3` values ('"+uid+"','"+name+"','"+hp+"','"+age+"')"
            cur.execute(sql)
            conn.commit()
            print('등록이 완료 되었습니다.')
        except Exception as e:
            print('등록에 실패 하였습니다. 다시 시도하십시오')
    
    elif answer == 2:
        cur.execute("select * from `user3`")
        conn.commit()
        print('아이디|이름|휴대폰|나이')
        for i in cur.fetchall():
            print("------------")
            print(f'{i[0]}|{i[1]}|{i[2]}|{i[3]}|')
    
    elif answer == 3:
        print('0: 나가기, 1: 아이디 검색, 2:이름 검색, 3:휴대폰 검색, 4:나이 검색')
        answer2 = input('선택 : ')
        
        sql = 'select * from `user3` where '

        if answer2 == '0':
            continue
        elif answer2 == '1':
            uid = input('검색 하실 아이디를 입력하시오. : ')
            sql += '`uid` like "%'+uid+'%"'
        elif answer2 == '2':
            name = input('검색 하실 이름을 입력하시오. : ')
            sql += '`name` like "%'+name+'%"'
        elif answer2 == '3':
            hp = input('검색 하실 휴대폰 번호를 입력하시오. : ')
            sql += '`hp` like "%'+hp+'%"'
        elif answer2 == '4':
            age = input('검색 하실 나이를 입력하시오. : ')
            sql += '`age` like "%'+age+'%"'
        else:
            print('알맞은 값을 입력하시오. 검색에서 나갑니다.')
            continue
        
        try:
            cur.execute(sql)
            conn.commit()
            print('아이디|이름|휴대폰|나이')
            for i in cur.fetchall():
                print("------------")
                print(f'{i[0]}|{i[1]}|{i[2]}|{i[3]}|')
        except:
            print('검색에 실패 했습니다.')
            
    elif answer == 4:
            uid = input('삭제 할 아이디를 입력하시오 : ')
            result = cur.execute('delete from `user3` where `uid`="'+uid+'"')
            conn.commit()

            if result > 0 :
                print('삭제가 완료 되었습니다.')
            else :
                print('삭제가 되지 않았습니다. 아이디를 다시 확인하여 주십시오.')
            
   
    else:
        print('0 ~ 4 중에서 입력하세요')


# 데이터 베이스 종료
conn.close()
print('프로그램 종료...')