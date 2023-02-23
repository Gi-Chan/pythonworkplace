import sys

n, k = map(int, sys.stdin.readline().split())
idx = 0
arr=[]
p_arr =[]
for i in range(1,n+1):
    arr.append(i)
    
while len(arr)>0:
    
    ## idx + 다음번에 제거할 인덱스
    # -1은 배열 크기가 줄었기떄문
    idx += k-1
    
    # idx가 배열보다 크거나 같다는건
    # 배열을 다 지니갔다고 보고 배열 길이만큼 나눈다.
    if idx >=len(arr):
        idx %=len(arr)
        
    p_arr.append(arr.pop(idx))

word =', '.join(map(str, p_arr)) 
print('<{}>'.format(word))