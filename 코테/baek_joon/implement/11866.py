
n, k = map(int, input().split())
que = [i for i in range(1,n+1)]
lst=[]
idx=0
while len(que) !=0:
    
    idx = (idx + k -1) % len(que) # 인덱스 범위 초과하는 걸 해결
    lst.append(que.pop(idx))

print('<', end='')
for i in lst:
    
    if i==lst[-1]:
        print(f'{i}>')
    else:
        print(f'{i}, ',  end='')