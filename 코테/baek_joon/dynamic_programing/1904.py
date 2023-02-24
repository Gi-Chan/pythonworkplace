n = int(input())
dp = [0 for i in range(n+1)]
dp[0] = 1
dp[1] = 2

"""
N이 
1일 때 1
2일 때 2
3일 때 3
4일 때 5

보면 피보나치임
"""

for i in range(2,n):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[-2]%15746)