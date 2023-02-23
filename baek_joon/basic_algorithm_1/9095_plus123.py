

'''

1을 만드는 경우 : 1 -> 1
2을 만드는 경우 : 2 -> 1+1, 2
3을 만드는 경우 : 4 -> 1+1+1, 1+2, 2+1, 3
4를 만드는 경우 : 3+1을 만드는 경우
                 2+2를 만드는 경우
                 1+3을 만드는 경우
                =1+2+3 =7
5를 만드는 경우 : 4+1을 만드는 경우는 1+4와 같음
                 3+2을 만드는 경우
                 2+3을 만드는 경우
                 1+4를 만드는 경우
'''

t=int(input())
dp = [0]*(11)
dp[1]=1
dp[2]=2
dp[3]=4
while t:
    n=int(input())

    for i in range(4, n+1):
        dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
    print(dp[n])
    t-=1
    