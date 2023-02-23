n = int(input())
part=0
for i in range(n+1): # 전체 영역 탐색
    arr = list(map(int, str(i))) # 1~n까지 숫자를 자리별로 만듬
    part = sum(arr) # 각 자리의 합을 더함

    if n==i+part: # 현재 숫자와 각 자리의 합이 n이면 종료
        print(i)
        break
    
    if i ==n:
        print(0)
    
