t = int(input())

# 문제의 조건은 이전층 같은 호와 같은층 이전 호의 합이다
"""    1호  2호 3호 4호 5호 6호
0층     1	2	3	4	5	6
1층     1	3	6	10	15	21
2층     1	4	10	20	35	56
3층     1	5	15	35	70	126
4층     1	6	21	56	126	252
예를 들어 1층 3호는 (0층 3호 + 1층 2호)
"""

for m in range(t):
    k = int(input())
    n= int(input())

    # k와 n의 최대값인 14를 저장할 이차원 배열 생성
    dp = [[i for i in range(1, n+2)] for j in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[k][n-1])

   