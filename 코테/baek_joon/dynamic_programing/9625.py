k = int(input())
"""
k	A	B
0	1   0
1	0	1	
2	1	1
3	1	2
4	2	3
5	3	5
6	5	8
7	8	13
8	13	21
9	21	34
10	34	55

a의 값은 이전 b의 값이고
b의 값은 b의 값들을 피보나치수로 한 값이다
b는 이전(a값 + b값)과 같음
"""
a_dp = [0 for i in range(k+1)]
a_dp[0] = 1
a_dp[1] = 0

b_dp = [0 for i in range(k+1)]
b_dp[1] = 1

for i in range(2, k+1):
    a_dp[i] = b_dp[i-1]
    b_dp[i] = b_dp[i-1] + b_dp[i-2]
    
print(a_dp[k], b_dp[k])