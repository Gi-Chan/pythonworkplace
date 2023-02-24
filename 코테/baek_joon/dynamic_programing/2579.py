s = int(input())
score = []
dp=[0 for i in range(s)]


for i in range(s):
    score.append(int(input()))

if s ==1:
    dp[0] = score[0] # 1번째 계단 점수
elif s==2:
    dp[0] = score[0] # 1번째 계단 점수
    dp[1] = score[0]+score[1] # score[1](2칸오르는거 뺀 이유)
# 이건 1칸씩 2칸 오르는게 가장 높을 수 밖에 없음
# dp[2] = max(score[0]+score[2], # 1칸 + 2칸
#             score[1]+score[2]) # 2칸 + 1칸

if s>2:
    dp[0] = score[0] # 1번째 계단 점수
    dp[1] = score[0]+score[1]
    for i in range(2,s):
        # 2칸 전에서 2칸오르는 점수 or 3칸 전에서 2칸+1칸 점수
        dp[i] = max(dp[i-2]+score[i], dp[i-3]+score[i-1]+score[i])
    print(dp[-1])

else:
    print(sum(score))
