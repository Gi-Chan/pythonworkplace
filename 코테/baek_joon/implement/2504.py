word = list(input())
stack = []
hap=1
result = 0
flag=0
"""
괄호를 열 때 hap이라는 변수의 값을 에 괄호에 따라 증가시킨다
hap 변수를 result에 넣는 조건은 반복문의 현재 i값 이전의 인덱스가
짝이 맞는 경우 (),[] 등 만 해당한다.

이 때, 값을 더해준 경우 괄호에 따라 hap의 변수를 감소시킨다.

ex)
([]) 이면 
처음 (에서 hap=2, result = 0
[ 에서, hap=6, result = 0
] 에서, hap=2, result = 6 (여기서 ]이전의 값이 [이기 때문에 더한 것)
) 에서, hap=1, result = 6 (여기서 result의 값이 변하지 않은 이유는
)이전의 값이 ]이기때문에 더하지 않은 것)

"""
for i in range(len(word)):
    
    if word[i] =='(':
        stack.append(word[i])
        hap*=2
    elif word[i] =='[':
        stack.append(word[i])
        hap*=3
    elif word[i] ==')':
        if not stack or stack[-1]=="[":
            result = 0
            flag=1
            break
        if word[i-1] == '(':
            result+=hap
        stack.pop()
        hap//=2
        
    elif word[i]==']':
        if not stack or stack[-1]  =='(':
            result = 0
            flag=1
            break
        if word[i-1] == '[':   
            result+=hap
        stack.pop()
        hap//=3
if stack:
    print(0)
else:
    print(result)

## 왜 print(0)을 위에 넣으면 안도니느거냐