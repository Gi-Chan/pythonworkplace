
'''

2 1 -4 3 4 -4 6 5 -5 1
idx 순서대로 합을 저장하는 배열을 만드는데

현재까지 합한 것과 다음 것을 더했을 때 다음값보다 작으면 선택안함
ex) hap = [2]
hap[3] = max(hap[2] -> 3 + -4 , -4) = -1
hap[4] = max(hap[3] -> -1 + 3, 3) = 3
여기서 살펴볼 것은 만약 이전수까지의 합+그다음 수보다 그 다음수가 크면
이전것을 날린다는 것을 알 수 있다.
    

'''
n=int(input())
nums = list(map(int, input().split())) #[10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
hap = [nums[0]]

for i in range(n-1):
    
    hap.append(max(hap[i]+nums[i+1], nums[i+1]))
print(max(hap))