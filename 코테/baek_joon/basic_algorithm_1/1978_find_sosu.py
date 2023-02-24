m,n = map(int, input().split())

def is_sosu(x):
    # x의 제곱근이 있다면 소수가 아니므로 (ex 9 = 3*3)
    # 탐색범위를 sqrt(x)까지 한다.
    for j in range(2,int((x**0.5))+1):
        if x%j==0:
            return False
    return True


for i in range(m, n+1):
    if i==1:
        continue
    
    if is_sosu(i):
       print(i)
