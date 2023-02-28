t=int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    # 보면 xx1호 선호도1, xx2호 선호도 2이거니까
    # n을 h로 나누면 선호하는 층수가 나올듯 -> 낮은층부터 차례대로 들어오니까
    floor = n%h # 선호하는 층
    
    if floor == 0: # 최고층이면 floor를 최고층으로 바꿈
        floor = h
        room = n//h
    
    else: # 최고층이 아니면 호수를 +1 해야함
        # n//h를 한 몫이 해당층이 가득찬 것을 의미하기떄문
        room = n//h +1
    
    
    print(floor*100+room)
