
t=int(input())

dp = [ [0,0] for _ in range(41)]

dp[0]=[1,0]
dp[1]=[0,1]
dp[2]=[1,1]

for i in range(3, 41):
    dp[i][0]= dp[i-2][0]+dp[i-1][0]
    dp[i][1]=dp[i-2][1]+dp[i-1][1]

for i in range(t):
    x = int(input())
    print(dp[x][0], dp[x][1])
    
