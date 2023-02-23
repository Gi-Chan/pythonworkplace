n = int(input())
pos = []

# pos에 x,y을 튜플로 저장
for i in range(n):
    x, y = map(int, input().split())
    pos.append((x,y))

  
#pos를 sorted하는데 x[0], 즉 x의 값만 보고 정렬

pos = sorted(pos, key=lambda x: x[0])

# x의 값만 보고 정렬된 리스트를 다시 y의 값만 보고 정렬
pos = sorted(pos, key = lambda x:x[1]) 

for j in range(n):
    print(pos[j][0], pos[j][1])