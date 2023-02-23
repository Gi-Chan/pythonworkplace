import sys
input = sys.stdin.readline
n = int(input())

boxes = list(map(int, input().split()))

# dp에는 각 자리마다 1개의 상자 개수를 설정한다.
dp = [1 for i in range(n)]

# 시작점에서는 1로 취급하고, 2번째부터 끝까지 비교한다.
for i in range(1,n):
    for j in range(i): # 각 번쨰? 각 몇번째마다 이전값을 비교하며
        if boxes[i]>boxes[j]: # 만약 해당 자리 값이 이전값들보다 크다면
            dp[i] = max(dp[i], dp[j]+1) # dp에 현재 dp값 or 이전 dp의 값들에 +1을 한 것 중 최대값을 넣는다
            
print(max(dp))