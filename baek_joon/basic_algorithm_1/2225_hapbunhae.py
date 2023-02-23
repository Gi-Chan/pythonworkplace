
'''
n+1의 경우의수
k=2일 떄
n이 홀수면 이전 것+1
n이 짝수면  {n/2의 경우} *2 +1

k=3이면 k-2경우의 모든 경우를 더하면 나옴


'''

# n, k =map(int, input().split())
n,k=20,2
dp = [[0 for _ in range(n)] for i in range(k+1)]

mod = 1000000000
# k=1이면 다 1로 초기화
for i in range(n):
    dp[0][i]=1



for i in range(1, k+1):
    
    for j in range(n+1):
        dp[i][j]=sum(dp[i-1][:j+1]) % mod
        
print(dp)