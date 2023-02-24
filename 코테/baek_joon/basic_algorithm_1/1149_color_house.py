
# h=3
h= int(input())

'''
h1,h2,h3에서 0,1,2 방문 인덱스 조작필요
-> 2차원 배열

'''
# ho = [[26,40,83],[49,60,57],[13,89,99]
#       ]
ho = []
for i in range(h):
    ho.append(list(map(int, input().split())))
for i in range(1,h):
    
    # [0,1,2] = [빨강, 파랑 초록]
    # 더하는 건 사용한 색깔 제외 가장 작은 값
    ho[i][0] +=min(ho[i-1][2], ho[i-1][1])
    ho[i][1] +=min(ho[i-1][2], ho[i-1][0])
    ho[i][2] +=min(ho[i-1][0], ho[i-1][1])

print(min(ho[h-1][0],ho[h-1][1],ho[h-1][2]))