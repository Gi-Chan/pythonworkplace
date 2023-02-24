

paper = int(input())
grid = [ [0 for i in range(101)] for i in range(101)]
hap = 0

"""
first
1. 검은색 종이의 넓이(100) x 종이 갯수(3)을 더한다
2. 한 검은 종이가 다른 종이와 겹치는 부분의 넓이를 뺀다.
ex (x1-x2+10) * (y2-y1+10)

하지만 위 방식을 사용하면 어느 종이가 큰지 작은지 구분해야하고
세 종이가 혹은 그 이상의 종이가 겹치는 부분의 구현이 복잡해진다.
따라서 flag 체크느낌의 방식으로 구현해봐야겠다.

second
이차원 배열을 생성해 0으로 초기화한다.
해당좌표의 (x,y)부터 (x+10, y+10)까지 다  1로 바꾼다
이차원 배열의 모든 숫자를 더한다 = 1로 체크된 부분만 넓이를 계산한다


"""

for i in range(paper):
    x,y = map(int, input().split())
    
    for j in range(x, x+10):
        for k in range(y, y+10):
            grid[j][k] = 1

for i in grid:
    hap += sum(i)
print(hap)