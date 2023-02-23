
word = input()
opp = []
result =''
'''
'('를 만나면 
')'를 만날때까지 숫자는 계속 넣고 연산자는 다른 스택에 넣는다
이 때, 연산자를 pop하며 추가한다.

'''
## 포인트.
## 연산자 우선순위에 따라 *나 /이면 +와 -를 다 넣는다는 점

for i in word:
    if i>='A' and i<='Z':
        result +=i
    
    else:
        
        # (는 그냥 넣음
        if i =='(':
            opp.append(i)
        
        # + 나 -가 나오면 
        elif i =='+' or i=='-':
            # 연산자 배열이 비어있지 않고 (가 아닐 때까지 다 추가함
            while opp and opp[-1] !='(':
                result += opp.pop()
            opp.append(i)
        
        elif i =='*' or i=='/':
             # 연산자 배열이 비어있지 않고 곱하기나 나누기가 아닐 때까지 다 추가함
            while opp and (opp[-1] =='*' or opp[-1]=='/'):
                result += opp.pop()
            opp.append(i)
            
        # 닫는 괄호가 나오면 여는 괄호가 나올때까지 다 추가하고
        # 여는 괄호도 뺀다.
        elif i == ')':
            while opp and opp[-1]!='(':
                result += opp.pop()
            opp.pop()
# 남은 연산자들을 뒤에서 넣는다.
while opp:
    result += opp.pop()    

print(result)    