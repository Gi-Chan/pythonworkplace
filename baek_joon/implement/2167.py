n, m = map(int, input().split())
grid = []
# 첫째 줄에 배열의 크기 N, M(1 ≤ N, M ≤ 300)이 주어진다. 
# 다음 N개의 줄에는 M개의 정수로 배열이 주어진다.
for i in range(n):
    grid.append(list(map(int, input().split())))

# 그 다음 줄에는 합을 구할 부분의 개수 K가 주어진다

"""
for t in range(k):
    sum = 0
    i, j, x, y = map(int, input().split())
    
    for k in range(i-1, x):
        for l in range(j-1,y):
            sum+=grid[k][l] 
    print(sum)
    
# 는 시간초과입니다.
# 누적합으로 계산해야하네요    
"""
dp = [ [0 for i in range(m+1)] for i in range(n+1)]


for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = grid[i-1][j-1] + dp[i-1][j] \
            + dp[i][j-1] - dp[i-1][j-1] 
k = int(input())
 
for t in range(k):
    i,j,x,y = map(int, input().split())
    
    print(dp[x][y] - dp[x][j-1]-dp[i-1][y]+dp[i-1][j-1])