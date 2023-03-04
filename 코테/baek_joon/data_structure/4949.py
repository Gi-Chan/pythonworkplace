
while True:
    word = input()
    if word =='.':
        break
    lst = [*word] # 이건 word안에 단어를 각각 분리
    flag=1 # yes or no를 체크할 플래그
    stack = [] # 스택
    for i in lst:
        
        if i == '(':
            stack.append(i)
        elif i ==')': # )가 나올 때, 스택이 있고 이전값이 (면
            if stack and stack[-1] == '(':
                stack.pop() # 짝이 맞으므로 뺀다
            else:
                flag=0 # 아니면 [ 이거나 스택에 없는데 닫는거니까 no
                break
        elif i =='[':
            stack.append(i)
        elif i ==']':
            if stack and stack[-1] == '[': # 위 설명과 동일
                stack.pop()
            else:
                flag=0
                break
        
    if not stack and flag: # 스택이 비었고 플래그가 1이면 yes
        print('yes') # 여기서 스택이 빈걸 왜 체크하냐? [. 입력하면 no인데 yes나옴
    else:
        print('no')