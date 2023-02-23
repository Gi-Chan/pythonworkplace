import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [ [0 for i in range(m+1)] for j in range(n+1)]

# 시작 좌표 지정
# dp[0][0] = arr[0][0]
# dp[0][1] = arr[0][1]
for i in range(n):
    for j in range(m):
        if i==0: # y좌표가 0이면
            dp[i][j] = dp[i][j-1] + arr[i][j]
        elif j==0: # x좌표가 0이면
            dp[i][j] = dp[i-1][j] + arr[i][j]
        else: # dp[x][y]의 값은 dp[x-1][y], dp[x][y-1], dp[x-1][y-1]중 가장 큰 값 선택
            dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[n-1][m-1])