def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)
n, k =map(int, input().split())
print(int(fact(n)/ (fact(n-k) * fact(k))))