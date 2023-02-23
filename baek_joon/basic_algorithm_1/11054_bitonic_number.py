n = int(input())

a = list(map(int, input().split()))

'''
증가, 감소는 11053,11722에서 구현했으므로 패스

sum은 무슨뜻이냐?
increase에서 각 단계마다 가지는 최대 길이를 구했고
decrease에서 각 단계마다 가지는 최소 길이를 구했다.
여기서 서로 같은 인덱스를 더하고 -1을 하면
증가하는 수열과 감소하는 수열의 길이를 구할 수 있다
1을 뺀 이유는 증가, 감소에서 뽑힌 값이 2번 카운트되기때문에
1을 뺀 것

'''

# 증가
dp = [0 for i in range(n)]
for i in range(n):
    
    for j in range(i):
        
        if a[i]>a[j] and dp[i] < dp[j]:
            dp[i]=dp[j]
        
    dp[i] +=1


# 감소
dp2= [0 for i in range(n)]

for i in range(n-1,-1,-1):
    
    for j in range(n-1,-1,-1):
        if a[i]>a[j] and dp2[i]<dp2[j]:
            dp2[i]=dp2[j]

    dp2[i]+=1

# 합
sum=[]
for k in range(n):
    sum.append(dp[k] + dp2[k]-1)

print(max(sum))