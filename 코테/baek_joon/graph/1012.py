import sys
sys.setrecursionlimit(10000)
# 이게 없으면 왜 오류가 나나 검색해봄
# https://hei-jayden.tistory.com/100
# 파이썬의 기본 재귀 한도는 1000이고, 재귀 깊이가 1000을 넘어갈 경우 모듈을 추가해야 한다 라고함


t = int(input())

# 여기선 그냥 dfs가 뭐냐?
# 배추를 없애는 기계임 그냥 트랙터
# 만약 dfs(0,0)을 돈다? 그럼 matrix[0][1], matrix[1][0] 이건 다 날라가는 거


def dfs(x, y):
    # 상하좌우 덧셈용
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]


    # 반복을 4번해야 상화좌우를 보겠죠
    for k in range(4):
        pos_x = x +dx[k]
        pos_y = y +dy[k]

        # position이 둘다 범위 안에 있으면 ㄱㄱ
        if (0 <= pos_x < m) and (0 <= pos_y < n):
            if matrix[pos_y][pos_x] ==1: # 이게 있다면 제거하고 다시 돌림
                matrix[pos_y][pos_x] = 0
                dfs(pos_x, pos_y) # 긍까 약간 발견되면 그걸 기점으로 또 있나 뻗어가는 과정이라고 생각
            
for loop in range(t):
    # 생성
    m, n, k = map(int, input().split())
    matrix = [ [ 0 for i in range(m)] for i in range(n)]
    for i in range(k):
        x,y = map(int, input().split())
        matrix[y][x] = 1


    # 검사
    ji = 0 # 지렇
    for i in range(m):
        for j in range(n):
            if matrix[j][i]==1: # 여기에 배추가 있으면
                dfs(i,j) # 이거 돌면서 이어진 배추를 다 제거함
                ji+=1 # 그래서 여기서 지렁이 + 하는거

    print(ji)