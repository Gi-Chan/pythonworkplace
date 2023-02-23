word = input()
word_list = word.split()
cnt=0
clr=0
pipe = -1
pipe_arr = []
# 구상
'''
1. 처음 '('는 레이저 작동이다.
2. '(' 를 만나면 파이프 수를 1개씩 증가 시킨다.
3. ')' 를 만날 때
    3.1 이전 것이 '('라면 레이저가 작동한다
        이 때, 현재 파이프 수 만큼 +를 한다.
    3.2 이전 것이 ')'라면 레이저는 작동하지 않는다.
        이 떄, 파이프 수는 -한다.
'''

for i in range(len(word)):
    pipe_arr.append(word[i])
    if word[i]=='(':
        clr+=1
        pipe+=1
    
    elif word[i]==')':
        clr-=1
        if word[i-1]=='(':
            cnt+=pipe
        else:
            cnt+=1
        pipe-=1

    if clr==0:
        pipe=-1
print(cnt)