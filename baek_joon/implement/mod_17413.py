k = int(input())


# 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로 나타낸다.
# 북쪽과 남쪽은 높이를 나타내므로 3,4는 높이
# 동쪽과 서쪽은 너비를 나타내므로 1,2는 너비

# 구상 : 높이와 너비의 max값을 곱해 전체 넓이를 구하고
# min값을 곲하고 빼서 넓이를 구하면 되지 않을까?
arr = [[],[]] # 0번 리스트에는 너비, 1번 리스트에는 높이
flag=0
direction, length = map(int, input().split())
if direction == 1 or direction == 2:
        arr[0].append(length)
        flag=1
elif direction == 3 or direction == 4:
    arr[1].append(length)

for i in range(1, 6):
    direction, length = map(int, input().split())
    
    # 너비는
    if direction == 1 or direction == 2:
        arr[0].append(length)
    
    elif direction == 3 or direction == 4:
        arr[1].append(length)

total_area = max(arr[0]) * max(arr[1])

if flag==1:
    part_area = arr[0][2] * arr[1][2]
else:
    part_area = arr[0][1] * arr[1][2]
result_area = total_area-part_area
print(result_area * k)