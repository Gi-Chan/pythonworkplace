import sys
input= sys.stdin.readline

'''
n번째줄의 i번은
1. 0이면 이전줄 0번+해당 값
2. 끝이면 이전줄 끝+해당 값
3. 나머지 경우는 이전줄 인덱스+-1중에 큰값 + 해당 값
'''
n=int(input())
# arr = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
arr=[]
dp=[ [0 for i in range(n)] for j in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))
    
dp[0][0] = arr[0][0]

if n==1:
    print(dp[0][0])
    exit()

dp[1][0] = arr[0][0]+arr[1][0]
dp[1][1] = arr[0][0]+arr[1][1]

if n==2:
    print(max(dp[1][0], dp[1][1]))
    exit()

for h in range(2,n):
    for m in range(h+1):
        if m==0: # 줄의 시작이면 이전줄 시작 + 현재 값
            dp[h][m] = dp[h-1][m]+arr[h][m]
        elif m==h: # 줄의 끝이면 이전줄 끝 + 현재 값
            dp[h][m] = dp[h-1][h-1]+arr[h][h]
            
        else: # 나머지 경우는 이전값 +-1중에 큰 값 + 현재 값
            dp[h][m] = max(dp[h-1][m-1], dp[h-1][m]) +arr[h][m]

print(max(dp[-1]))