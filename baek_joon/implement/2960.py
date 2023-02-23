n, k = map(int, input().split())

sieve = [ i for i in range(2,n+1)]
cnt=0
flag=0
while len(sieve) != 0:
    
    num = sieve.pop(0)
    cnt+=1
    
    if flag==1:
        print(su)
        break
    if cnt==k:
        print(num)
        break
    for i in sieve:
        if i % num ==0:
            sieve.remove(i)
            cnt+=1
        
        if cnt==k:
            su=i
            flag=1
            break
    