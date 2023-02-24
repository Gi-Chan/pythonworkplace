import sys
n= int(sys.stdin.readline())

while n>0:
    words = list(sys.stdin.readline().split())

    for i in words:
        word = list(i)
        
        
        for j in reversed(range(len(word))):
            print(word[j], end='')
        print(' ', end='')
    n-=1
    print()