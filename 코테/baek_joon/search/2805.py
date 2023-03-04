n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end=max(tree)

while start<=end: # 이분 탐색 종료지점ㅁ
    
    # 중간값
    mid = (start + end) // 2
    result=0 # 잘린 나무의 합
    for i in tree:
        if i >=mid: # 현재 나무가 잘린부분보다 클떄만
            result+= (i-mid) # 잘린 나무를 더함
    
    if result >=m: # 이 결과값이 최적이 아닐 수 있기 때문에 시작점을 증가시켜 다시 실행
        start = mid+1 # 
    else:
        end = mid -1 # 잘린 나무의 합이 원하는 m값보다 작다면 최대 높이를 줄인다.
    
print(end)