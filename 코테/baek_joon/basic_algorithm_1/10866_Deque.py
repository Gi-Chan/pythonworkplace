
import sys
deque =[] 
word=[]

n = int(sys.stdin.readline())

for i in range(n):
    com = sys.stdin.readline().split()
    
    if com[0]=='push_front':
        deque = [com[1]]+deque
    elif com[0]=='push_back':
        deque.append(com[1])
    
    
    elif com[0]=='pop_front':
        if len(deque)>0:
            print(deque.pop(0))
        else:
            print(-1)
    
    elif com[0]=='pop_back':
        if len(deque)>0:
            print(deque.pop())
        else:
            print(-1)            
            
    elif com[0]=='size':
        print(len(deque))
        
    elif com[0]=='empty':
        if len(deque)>0:
            print(0)
        else:
            print(1)
            
            
    elif com[0]=='front':
        if len(deque)>0:
            print(deque[0])
        else:
            print(-1)
    elif com[0]=='back':
        if len(deque)>0:
            print(deque[-1])
        else:
            print(-1)
    
