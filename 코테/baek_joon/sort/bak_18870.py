import sys
n = int(sys.stdin.readline())


nums = list(map(int, sys.stdin.readline().split()))
# 탐색 크기를 줄이기 위해 set
se_num = sorted(list(set(nums)))

dict = {}
for i in range(len(se_num)):#nums의 시작부터 돌면서
    # 딕셔너리에 se_num[i]의 값을 key로
    # value를 정렬된 순서로 넣는다
    # se_num에 0번값은 제일 작은 숫자이기 때문
    # 1번값은 그 다음으로 큰수
    dict[se_num[i]]=i

for i in nums:
    # 사전에 시작 값은 가장 작은 key이므로
    print(dict[i], end=' ') 


# 시간 초과
'''
# 단순히 숫자 비교만을 해야 하므로 set을 사용하자
nums = list(map(int, sys.stdin.readline().split()))
se_num = list(set(nums))
for i in nums:#nums의 시작부터 돌면서
    cnt=0
    for j in range(len(se_num)): # 중복값을 없앤 nums와 비교
        # nums에 숫자가 set한 것 과 만나면 카운트 안함
        if i ==se_num[j]:
            continue
        # i가 set한 숫자들과 비교해서 몇번째인지 구함
        elif i>se_num[j]:   
            cnt+=1
    print(cnt, end=' ')        
'''