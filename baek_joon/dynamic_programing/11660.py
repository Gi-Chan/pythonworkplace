import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [ list(map(int, input().split())) for i in range(n)]
# # arr = [[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]
dp = [ [0 for i in range(n+1)] for i in range(n+1)]
# for i in range(n):
#     print(arr[i])

# https://castlerain.tistory.com/100 이 사이트 그림 참고했음

# 누적합 부분
for i in range(n):
    for j in range(n):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]) + arr[i][j]
        # i+1 j+1의 누적합은 = 전체 크기 - 빼야할 직사각형 2개 + 직사각형 2개를 뺀 부분 더해주기
for k in range(m):
    # 좌표입력
    x1, y1, x2, y2 = map(int, input().split())
    x1-=1 # 인덱스는 0부터 시작하므로 1씩 빼줘야함
    y1-=1
    x2-=1
    y2-=1
    # 누적합 부분 그대로 출력
    print(dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1]) + dp[x1-1][y1-1])    






