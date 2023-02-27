import sys
input = sys.stdin.readline
N =int(input())
arr= set(list(map(int, input().split())))
M = int(input())
arr2 = list(map(int, input().split()))

for i in range(M):
    if arr2[i] in arr:
        print(1)
    else:
        print(0)
        

