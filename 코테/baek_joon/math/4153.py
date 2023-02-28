

while True:
    a,b,c  = map(int, input().split()) # a,b,c 를 입력받음
    arr = [a,b,c] # 리스트에 a,b,c 를 넣음
    arr = sorted(arr) # 정렬함 그럼 최대값(빗변)이 마지막으로 가겠죠

    if 0 in arr: # 근데 리스트에 0이있다? 그럼 종료
        break

    # 피타고라스 정의가 맞으면 참 아니면 거짓
    if arr[2]*arr[2] == arr[0]*arr[0] + arr[1]*arr[1]:
        print('right')
    else:
        print('wrong')
