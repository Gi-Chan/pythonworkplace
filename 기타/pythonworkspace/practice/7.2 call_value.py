def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금 함수
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금 함수
    if balance >= money: # 잔액이 출금액보다 많으면
        print("{0}원 출금이 완료되었습니다. 잔액은 {1}원 입니다.".format(money, balance - money))
        return balance, money

    else: # 잔액이 출금액보다 적으면
        print("{0}원 이상을 출금할 수 없습니다.".format(balance))
        return balance
    
def withdraw_night(balance, money, commision):

    return  balance - money - commision, money, commision

balance = 0 # 처음 금액
balance = deposit(balance, 1000)
# blance = withdraw(balance, 100)
balance, money, commision = withdraw_night(balance, 500, 100)
print("수수료는 {0}원이며 {1}원 출금 후 잔액은 {2} 원입니다.".format(commision, money, balance))
