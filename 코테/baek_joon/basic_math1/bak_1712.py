a,b,c = map(int, input().split())


## 생산 비용이 이익보다 크면 -1
if(b >= c):
    print(-1)

else:
    print(a//(c-b)+1)

