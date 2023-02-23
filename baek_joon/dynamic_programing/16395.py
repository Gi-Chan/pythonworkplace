n, k = map(int, input().split())

# n번째 줄에는 n개의 수가 있으므로 dp공간은 (n+1)^2 으로 생성
dp = [[1 for i in range(n+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i-1):
        if j!=0 or j!=i: # 각 행의 처음과 끝을 제외하고
            dp[i][j] = dp[i-1][j]+dp[i-1][j-1] # 이전 행 값의 (현재 인덱스값 + 이전 인덱스)
            # 위 덧셈이 파스칼의 삼각형을 만족함

    
print(dp[n][k-1])