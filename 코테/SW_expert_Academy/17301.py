# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYffJQbab3wDFARP&categoryId=AYffJQbab3wDFARP&categoryType=CODE

t = 1

# 기본적으로 주어진 수열에 대해서는 아니네
for i in range(t):
    dp=[]*100000
    n=3 # 입력 받은 초기 수열
    n_lst = list(map(int, input().split()))
    q = 5 # 찾아야하는 수열의 인덱스
    q_lst = list(map(int, input().split()))
    
    # dㅔ 초깃값 설정
    dp = [n_lst[i] for i in range(len(n_lst) )]

    # dp를 이용해 이전 합들을 저장해 연산횟수를 줄이자.

    # q_lst의 최댓값 까지만 n_lst만 갱신하면 된다.
    for k in range(len(n_lst), max(q_lst)):
        if k == len(n_lst):
            dp[k] = sum(n_lst)
        n_lst[k] = dp[k-1]
    
    ## 포기