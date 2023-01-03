"""
날짜 : 2023/01/03
이름 : 심규영
내용 : A+B-7, 11021번 문제
"""

import sys
for i in range(int(input())):
    print('Case #',i+1,': ',sum(map(int,sys.stdin.readline().split())),sep="")