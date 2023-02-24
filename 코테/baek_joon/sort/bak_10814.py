import sys
n = int(sys.stdin.readline())
arr=[]

for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    arr.append((int(age),name))

parr = sorted(arr, key=lambda x:x[0])

for j in range(n):
    print(parr[j][0], parr[j][1])