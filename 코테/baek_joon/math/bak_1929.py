## time out
m, n = map(int, input().split())

for i in range(m,n+1):
    if(i==2):
        print(i)
        
    cnt=0
 
    for j in range(2,i):
        if i%j==0:
            cnt+=1
        
    if cnt==0:
        print(i)