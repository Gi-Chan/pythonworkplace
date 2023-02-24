n = int(input())

child = []
for i in range(n):
    child.append(int(input()))

"""
3526147
2356147
1235647

1. 제일 큰 수는 가장 뒤로 보낸다
2.  시작 인덱스를 min으로 잡고 뒤로 탐색하면서
    min보다 작은 값이 나오면 교체하고 cnt 증가
"""

# 배열에서 가장 큰 값을 가장 뒤로 보낸다
child.append(child.pop(child.index(max(child))))
cnt = 1
mini = 0


for i in range(n):
    mini = child[i]
    for j in range(i, n):
        if mini>child[j]:
            child.insert(i, child[j])
            child.pop(j+1)
            cnt+=1

print(cnt)  