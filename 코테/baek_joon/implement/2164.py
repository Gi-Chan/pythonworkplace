from collections import deque
# 참고 : https://mong9data.tistory.com/118

n=int(input())
arr=[ i for i in range(1,n+1)]

deque1 = deque(arr)

for i in range(n-1):
    deque1.popleft() # 제일 위에 있는 카드를 바닥에 버린다.
    deque1.append(deque1.popleft()) # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

print(deque1[0])