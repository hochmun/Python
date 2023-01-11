"""
날짜 : 2023/01/11
이름 : 심규영
내용 : 파이썬 상속 실습
"""

from sub1.StockAccount import StockAccount

kb = StockAccount('kb증권','101-12-1001','홍길동',5000,'삼성전자',10,60000)
kb.deposit(1000000)
kb.sell(5, 65000)
kb.show()