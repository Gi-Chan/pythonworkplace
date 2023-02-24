
'''
# 최대 공약수
while min!=0:
    max =max %min
    max,min = min,max
print(max)
    
# 최소 공배수
print(int(a*b/max))

여기선 lcm 사용

'''
# 최대 공약수
def gcm(x,y):
    while y!=0:
        x =x %y
        x,y = y,x
    return x

# 최소공배수
def lcm(x,y):
    out = (x*y)/gcm(x,y)
    return int(out)

t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    print(lcm(a,b))