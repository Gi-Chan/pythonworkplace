
sosu = [1] * 1000001
sosu[0] = sosu[1] = 0

# 소수 구하는 부분
for i in range(2,1000001):
    if sosu[i]:
        sosu.append(i)
        for j in range(i+i, 1000001, i):
            sosu[j] = 0

while 1:
    n = int(input())
    
    if n==0:
        break
    
    for i in range(len(sosu)):
        if sosu[i] > n//2:
            break
        if sosu[i] and sosu[n-i]:
            print("{} = {} + {}".format(n, sosu[i], sosu[n-i]))
            break