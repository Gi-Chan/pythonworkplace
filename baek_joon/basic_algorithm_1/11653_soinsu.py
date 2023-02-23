n=int(input())

if n==1:
    exit()

## n이 0이 아닐 때까지 출력
while n!=0:
    
    ## n보다 작은 수 i로 나눠지면 출력
    for i in range(2,n+1):
        if n%i==0:
            print(i)
            break
    # 찾은수 i만큼 나눔
    n= int(n/i)