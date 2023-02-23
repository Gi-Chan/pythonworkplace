import sys

def recursion(str, a, b, cnt):
    
    if(a >= b) :
        return 1, cnt
    elif str[a] != str[b]:
        
        return 0, cnt
    else: 
        cnt+=1
        return recursion(str, a+1, b-1, cnt)

def isPalindrome(s):
    cnt=1
    return recursion(s, 0, len(s)-1, cnt)
global cnt

n = int(sys.stdin.readline())
for i in range(n):
    str = sys.stdin.readline().rstrip()
    pr = isPalindrome(str)
    print(pr[0], pr[1])

