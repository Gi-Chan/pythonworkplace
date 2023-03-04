import math
a,b,v = map(int, input().split())
k = math.ceil((v-b)/(a-b)) # 올림
print(k)
    
    