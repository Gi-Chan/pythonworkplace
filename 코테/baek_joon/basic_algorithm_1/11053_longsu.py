n=int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]

'''
a = [10,20,10,30,20,50]
dp = [0 ,0 ,0 ,0 ,0 ,0 ]
i,j (j<i)
여기서 a[i]가 a[j]보다 큰 경우에만 실행한다
그리고 dp[i]가 dp[j] 보다 작아야한다.

왜냐
일단 값이 큰 경우에만 +를 해야함(a[i]>a[j])
그리고 dp[i]가 그 이하의 경우를 돌며
자신보다 크면 일단 자기가 숫자가 크니까
해당 번호의 길이+1을 하면 되기 떄문

'''

for i in range(n):
    
    for j in range(i):
        
        if a[i]>a[j] and dp[i] < dp[j]:
            dp[i]=dp[j]
        
    dp[i] +=1

print(max(dp))