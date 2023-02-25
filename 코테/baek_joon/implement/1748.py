
n=int(input())
w = len(str(n))
sum=0
last = (n-(10**(w-1))+1)*w
for i in range(0, w-1):
    sum += 9 * (10**i)*(i+1)
    
print(sum+last)

