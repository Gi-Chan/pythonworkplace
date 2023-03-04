x, y, w, h = map(int, input().split())
sum=[]

sum.append(h-y)
sum.append(y)
sum.append(w-x)
sum.append(x)

print(min(sum))