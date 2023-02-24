n= int(input())
arr = []
dp=[0 for i in range(n+1)] # dp배열 생성 이익 계산을 담당함

for i in range(n):
    arr.append(list(map(int, input().split())))
## 여기까지 입력 받는 부분

for i in range(n): # n번 반복을 하는데
   for j in range(i+arr[i][0], n+1):
       # i+arr[i][0](상담을 하는데 걸리는 기간)과 n+1(전체기간)
       # 을 돈다. 이렇게 하면 모든 경우의 수를 볼 수 있음
       
       # 여기서 dp[j]의 뜻은 i번째 날짜에 해당 상담을 하고 얻는 이익을 저장한다
       if dp[j] < dp[i] + arr[i][1]:
           # 만약 i번째 상담을 선택하고 돈을 버는게
           # 이전 상담을 한 돈보가 크다면
           dp[j] = dp[i] + arr[i][1] 
           # j일에 얻을 수 있는 가장 큰 이익을 i번 일을 받는것으로 변경한다

print(dp[-1])