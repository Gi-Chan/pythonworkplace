
class Balance:

    def __init__(self, bal=0):
        self.__balance = bal
    
    def withdraw(self, money):
        self.__balance-=money
        print(f"통장에 {money} 가 출금되었음")
        self.__balance -= money
    
    def deposit(self, money):

        print(f"통장에 {money} 가 입금되었음")
        
        self.__balance -= money
    
my = Balance(10)
my.withdraw(10)
my.deposit(100)
