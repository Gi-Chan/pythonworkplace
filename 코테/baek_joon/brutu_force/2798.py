import sys
input = sys.stdin.readline
n,m = map(int, input().split())
max=0 # 최고값
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = arr[i] + arr[j] + arr[k]
            if sum <= m and sum >= max:
                max = sum

print(max)        