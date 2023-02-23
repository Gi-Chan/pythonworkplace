


def fact(n):
    result=1
    for i in range(1, n+1):
        result= result*i
    return result

n, k = map(int, input().split())
print((fact(n)//(fact(n-k) * fact(k)))%10007)
