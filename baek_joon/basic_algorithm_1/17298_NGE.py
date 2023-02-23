## 이해하고 올리기
import sys
n=int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

arr = [-1]*n
stack=[]

for i in range(n):
    
    while stack and nums[stack[-1]]<nums[i]:
        arr[stack.pop()] = nums[i]
    stack.append(i)
for i in arr:
    print(i, end=' ')