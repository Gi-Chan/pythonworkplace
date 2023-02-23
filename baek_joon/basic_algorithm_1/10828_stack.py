import sys

n=int(sys.stdin.readline())
arr =[]

while(n>0):
    ins = sys.stdin.readline().split()
    
    if ins[0]=="push":
        arr.append(ins[1])
    elif ins[0]=="pop":
        if len(arr) >0:
            print(arr.pop())
        else:
            print(-1)
    elif ins[0]=="size":
        print(len(arr))
        
    elif ins[0]=="empty":
        if len(arr)>0:
            print(0)
        else:
            print(1)
    elif ins[0]=="top":
        if len(arr)>0:
            print(arr[-1])
        else:
            print(-1)
    n-=1