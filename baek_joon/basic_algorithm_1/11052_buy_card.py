n = int(input())
price = [0] + list(map(int, input().split()))

dp = [max(price)] *(n+1)
dp[0]=0

'''
dp[i] = 카드 i개를 구매할 수 있는 최대가격
price[k] = k개가 들어있는 카드팩의 가격

dp[i] = max(dp[i],price[k] + dp[i-k])
i개 카드를 사는 최대가격 = k개 카드팩가격 + i-k개의 카드
를 사는 최고 가격

'''

for i in range(n+1):
    for j in range(i+1):
        dp[i] = min(dp[i], dp[i-j]+price[j])
print(dp[i])


'''
card = int(input()

p_i의 가격을 카드개수로 나누면
카드팩 i의 카드 1개당 가격이 나온다
이중 가장 비싼걸 우선시하며 고르자.



## 틀린이유 10 / 1 100 160 1 1 1 1 1 1 1 
## 33 22를 선택하는게 최대지만 3331로 선택이됨
# 즉 각 단계에서 최선을 선택했던것이고
# 그 다음단계까지 생각을 하지 못함


price = list(map(int, input().split()))

value = [0]*(card)
for i in range(card):
    value[i] = price[i]/(i+1)
sum=0 # 가격

while card!=0:
    
    # 남은 카드개수 이상을 선택하지않게 슬라이싱
    value = value[0:card]

    # value중 가장 큰것의 인덱스 +1 만큼 카드수를 뺀가
    # 인덱스는 0부터 시작하니까 +1 한 거
    card -= (value.index(max(value))+1)
    
    # 마찬가지로 가격은 price[value중 가장 높은 것의 인덱스]
    sum+=price[value.index(max(value))]
print(int(sum))
'''