
n = int(input())
arr = [] 
result = [] # 결과를 담을 배열
for i in range(n):
    # 2차원 리스트 입력받기
    arr.append(list(map(int, input().split())))

for i in range(n):
    rank = 1 # 등수
    for j in range(n):
        # i번째 사람보다 작은 사람이 있으면 rank 증가
        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            rank+=1
    result.append(rank)

# 출력
for i in range(len(result)):
    print(result[i], end=" ")