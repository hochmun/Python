from sub1.Account import Account

class StockAccount(Account):
    
    def __init__(self, bank, id, name, balance: int, stock, amount, price):
        super().__init__(bank, id, name, balance)
        self._stock = stock
        self._amount = amount
        self._price = price

    def sell(self, amount, price):
        self._balance += amount * price
        self._amount -= amount

    def buy(self, amount, price):
        self._balance -= amount * price
        self._amount += amount

    def show(self):
        super().show()
        print('주식종목 :', self._stock)
        print('주식수량 :', self._amount)
        print('주식가격 :', self._price)
