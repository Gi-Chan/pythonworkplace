import sys
input = sys.stdin.readline
n= int(input())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [ [0 for i in range(n)] for j in range(n)]

# 시작좌표에서는 1번 이동을 한걸로 한다
dp[0][0]=1

for i in range(n):
    for j in range(n):
        
        if i==n-1 and j==n-1:
            print(dp[i][j])
            break
        
        # arr[i][j]에서 i혹은 j가 arr[i][j]만큼 점프할 때 n보다 작아야함
        if (i+arr[i][j]<n) :
            dp[i+arr[i][j]][j] +=dp[i][j]
        if (j+arr[i][j])<n:
            dp[i][j+arr[i][j]] +=dp[i][j]
         
    