k, n = map(int, input().split())
lans = []
for i in range(k):
    lans.append(int(input()))

start, end = 1, max(lans)

while start<=end:
    
    mid = (start + end) // 2
    cnt=0
    for lan in lans:
        cnt+=lan//mid

    if cnt >= n:
        start = mid +1
    else:
        end = mid -1
print(end)