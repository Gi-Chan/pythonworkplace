


'''
다이나믹 없이 생각해보면
n입력 받아서 그거 다 쪼갠다음

i가 i+!보다 작거나 같으면 ok하면 되는거 아닌가.

이거 그건데 앞자리가 0이면 0인경우
1~9면 i or i+1인경우 더하는거

'''
n=int(input())
dp = [[0 for i in range(10)] for i in range(n+1)]
mod = 10007

for i in range(10):
    dp[0][i] = 1

for i in range(1,n+1):
    
    
    for j in range(10):
        dp[i][j]= (sum(dp[i-1][j:]))%mod

print(dp[n][0]%mod)
