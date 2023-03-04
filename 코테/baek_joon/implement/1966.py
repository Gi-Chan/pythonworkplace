t = int(input())
# 참고 : https://assaeunji.github.io/python/2020-05-04-bj1966/
for i in range(t):
    n, m = map(int, input().split())
    pri = list(map(int, input().split()))
    idx = list(range(len(pri)))
    idx[m] = 'this' # 이게 원하는 값
    
    cnt=0 # 몇번째에 있는지 체크하는 함수
    
    while True:
        
        if pri[0] == max(pri):
            cnt+=1
            
            if idx[0] == 'this':
                print(cnt)
                break
            else:
                pri.pop(0)
                idx.pop(0)
        else:
            pri.append(pri.pop(0))
            idx.append(idx.pop(0))
        
    