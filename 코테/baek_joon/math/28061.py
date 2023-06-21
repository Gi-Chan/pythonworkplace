n=int(input())
lemon = list(map(int, input().split()))


for i in range(len(lemon)):
    lemon[i] -= (len(lemon)-i)
print(max(lemon))