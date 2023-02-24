# 15761. 크고 작은 이진수의 곱셈 
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYQHbyrq-JkDFATW&categoryId=AYQHbyrq-JkDFATW&categoryType=CODE


# 구상
'''
B가 0이면 최댓값과 최솟값이 같으니까 A의 개수
B가 1보다 클 때,
    1. A가 1이면 1은 맨앞 고정이므로 A
    2. A가 1이 아닌 값이면 M,N의 1은 각각 A개씩 들어가므로
        A*2
'''
T = int(input())

for t in range(T):
    A,B = map(int, input().split())
    
    if B==0:
        print(A)
    
    elif B>=1:
        if A==1:
            print(A)
        else:
            print(A*2)
    

