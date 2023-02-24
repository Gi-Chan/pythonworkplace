arr = []
for i in range(9):
    arr.append(int(input()))
flag = 0 
hap = sum(arr) - 100 # 난쟁이의 합이 100이라고 함
j=0
for i in range(9):
    
    for j in range(i):
        if arr[i] + arr[j] == hap: # i와 j인덱스의 난쟁이가 9명의 합 - 100과 일치하면 가짜
            flag = 1
            break
    if flag ==1: # 플래그가 1이면 100이 아닌 애들 2명을 찾은 거
        arr.pop(i)            
        arr.pop(j)
        break
arr =sorted(arr) # 배열 오름차순 정렬

for i in range(len(arr)):
    print(arr[i], end="\n")


