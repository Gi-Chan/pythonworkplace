import sys

n= int(sys.stdin.readline())


for i in range(n):
    cnt=0

    word = sys.stdin.readline()
    for j in range(len(word)):
        if word[j] =='(':
            cnt+=1
        elif word[j]==')':
            cnt-=1
        if cnt<0:
            print("NO")
            break
    
    
    if cnt==0:
        print("YES")
    elif cnt>0:
        print("NO")
