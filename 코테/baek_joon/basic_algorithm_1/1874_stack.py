import sys

stack =[] 
in_stack=[] # 스택에 있는 수
word=[]

cnt = 1
n = int(sys.stdin.readline())

for i in range(n):
    num = int(sys.stdin.readline())
    
    while(num >=cnt):
        in_stack.append(cnt)
        word.append('+')
        cnt+=1
    
    if num == in_stack[-1]:
        word.append('-')
        in_stack.pop()
    
    else:
        print('NO')
        sys.exit()
    
for j in word:
    print(j)

## 시간초과
"""import sys

stack =[] 
in_stack=[] # 스택에 있는 수
word=[]
# 처음 숫자는 스택에 다 넣기

n = int(sys.stdin.readline())

for i in range(n):
    num = int(sys.stdin.readline())
    if len(in_stack)==0:
        in_stack.append(1)
        word.append('+')
    
    if in_stack[-1]==num:
        word.append('-')
        stack.append(in_stack.pop())
        

    
    elif in_stack[-1] < num:
        for j in range(in_stack[-1],num+1):
            
            if j in stack:
                pass
            elif j not in in_stack :
                word.append('+')
                in_stack.append(j)
        word.append('-')
        stack.append(in_stack.pop())
            
    else:
        print("불가능")
        sys.exit()

for k in word:
    print(i)
    """
    