

'''
[0,1]을 true, false로 설정해서 플래그가 있는거만 넣으면?

dp[1] = 1 -> 1
dp[2] = 1 -> 10
dp[3] = 2 -> 100 101
dp[4] = 3 -> 1000, 1001 1010
dp[5] = 5 -> 10000, 10001 10010 10100 10101 (0뒤에 붙이는거 3개, 1뒤에 1개)
dp[6] = 8 -> 100000, 100001, 100010, 100100
             100101, 101000, 101001, 101010

왜 피보나치가 보이냐

0으로 끝나면 0, 1 붙일 수 있음, 1로 끝나면 뒤에 0 붙일 수 있음(앞은 중복임)
'''
n=int(input())
dp = [0 for _ in range(91)]

dp[1]=1
dp[2]=1

for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
    
print(dp[n])