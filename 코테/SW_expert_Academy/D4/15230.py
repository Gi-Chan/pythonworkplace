# 15230 알파벳 공부
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYLnMQT6vPADFATf


# 구상
'''
a,b,c,...,z는 아스키코드로 97~122이다.
반복문을 돌리는데
check= 아스키코드 시작 ++1하면서
문자열이 아스키코드값과 일치하면 체크


'''



t = int(input())

for t in range(t):
    word=''
    word = input().rstrip()
    cnt = 0
    check = 97
    for i in range(len(word)):
        if ord(word[i])==check:
            cnt+=1
        else:
            break
        check+=1

    print(cnt)