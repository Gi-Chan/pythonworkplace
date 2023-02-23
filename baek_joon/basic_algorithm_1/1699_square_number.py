
n=int(input())


dp = [ 0 for _ in range(n+1)]
square = [ i * i for i in range(1,n+1)]

for i in range(1, n+1):
    arr=[]
    for j in square:
        if j>i:
            break
        # 아래 설명 참조
        arr.append(dp[i-j])
    dp[i] = min(arr)+1
        
        
print(dp[n])

'''
dp[i-j]란?
j는 square배열인데 1, 4, 9, 16 ... n*n이다.

i가 j보다 클 경우 arr배열에 dp[i-j]를 추가하는데
i=3이라면
dp[3-1 =2], 즉 2를 만드는 수에서 +1을 하겠다는 뜻

i=9
여기서 dp는
dp[o] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 1
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 2

j = 1, 4, 9
dp[9-1 = 8] 1^2 쓰는 경우
dp[9-4 = 5] 2^2 쓰는 경우
dp[9-9 = 0] 3^2 쓰는 경우 중에
3^2을 쓰면 dp[0]이므로 최소의 경우가 될것이다



만약 i=16이라면
j는 1, 4, 9, 16 이렇게 4가지 경우가 있고
dp[16-1 = 15] 1^2 쓰는 경우
dp[16-4 = 12] 2^2 쓰는 경우
dp[16-9 = 7] 3^2 쓰는 경우
dp[16-16 = 0] 4^2 쓰는 경우

여기서도 dp[0]이 최소의 경우이다


'''