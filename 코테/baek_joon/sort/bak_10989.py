import sys
# 참고 https://www.acmicpc.net/board/view/26132
'''
이게 처음에 천만숫자를 배열에 다 넣는다고 생각했는데 8MB면
8*10^6byte 약 800만 바이트므로 전체 저장은 불가함

그래서 들어오는 숫자가 1~10000까지의 숫자이니까
해당 숫자 배열을 만들고 입력값이 있으면 카운팅하는 식으로 했다.

ex) space = [0,0,0,0,...0]
1입력 -> [1,0,0,0,...0]
1입력 -> [2,0,0,0,...0]
3입력 -> [1,0,1,0,...0]
이런식

입력을 다 받으면 
space 배열을 돌며 0인경우는 패스하고
숫자가 있을 경우 해당 숫자를 카운팅만큼 출력한다.
'''

input = sys.stdin.readline
space = [0]*10001
n=int(input())

for i in range(n):
    space[int(input())]+=1 # 카운팅

for i in range(10001):
    if space[i] != 0: # 0이면 패스
        for j in range(space[i]): # 카운팅 숫자만큼 출력
            print(i)