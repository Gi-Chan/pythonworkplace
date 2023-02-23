import sys
n = int(sys.stdin.readline())
arr=[]
for i in range(n):
    word = sys.stdin.readline()
    arr.append(word)

parr = sorted(set(arr))
parr = sorted(parr, key=len)


for j in parr:
    print(j, end='')