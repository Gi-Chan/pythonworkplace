n= int(input())

for i in range(n, 0, -1):
    if i<n:
        print(" "*(n-i), end="")
    
    print("*"*i)