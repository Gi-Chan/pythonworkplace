'''
n은  n과 n-1제외 n-2까지 더한값,  
n-1까지 더한 값, n-2제외 n-1까지 더한 값

정리하면 n=4
4은 전까지의 최대값,  dp[4-1]
전전까지 최대 + 현재값, dp[4-2] + arr[4]
전전전까지 최대 + 전 + 현재값, d[4-3] + arr[i-1] + arr[i]


'''
import sys
input = sys.stdin.readline

n=int(input())

dp = [0 for i in range(n)]
# arr = [6,10,13,9,8,1]
arr= []
for i in range(n):
    arr.append(int(input()))

if n==1 or n==2:
    if n==1:
        print(arr[0])
        exit()
    elif n==2:
        print(arr[0]+arr[1])
        exit()
    
dp[0]=arr[0]
dp[1]=arr[0]+arr[1]
dp[2]=max(arr[0]+arr[2], arr[1]+arr[2], arr[0]+arr[1])


for i in range(3,n):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])

print(max(dp))