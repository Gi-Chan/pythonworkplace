t= int(input())


for j in range(t): # t 번 반복
    n, m = map(int, input().split())

    # 조합은 nCr일 경우 n!/((n-r!)r!)이다
    n_fact = 1 
    n_r_fact = 1
    r_fact =1
    for i in range(1, m+1): # n! 계산
        n_fact*=i

    for i in range(1, m-n+1): # n-r! 계산
        n_r_fact*=i
        
    for i in range(1, n+1): # r! 계산
        r_fact*=i


    print((n_fact)//(n_r_fact*r_fact))