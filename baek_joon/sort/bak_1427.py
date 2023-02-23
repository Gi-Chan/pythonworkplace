n = int(input())
arr=[]
for i in map(int, str(n)):
    arr.append(i)

parr = list(reversed(sorted(arr)))

for j in range(len(parr)):
    print(parr[j], end='')