n=int(input())

dp = [[0] *10 for i in range(n+1)]


# 초기 n=1일때는 1가지 밖에 없음
for i in range(1,10):
    dp[1][i]=1


for i in range(2, n+1):
    for j in range(10):
        
        # 앞자리가 0이면 이전 것이 1인경우만 있음
        if j==0:
            dp[i][j]=dp[i-1][1]
        
        # 앞자리가 9인 경우는 이전 것이 8인 경우
        elif j==9:
            dp[i][j] =dp[i-1][8]
            
        # 나머지 경우는 이전수 +-1의 경우의 수
        else:
            dp[i][j]= dp[i-1][j-1]+dp[i-1][j+1]
print(sum(dp[n])%1000000000)