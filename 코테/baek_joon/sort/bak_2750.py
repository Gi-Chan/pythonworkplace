
## 이게 더 빠름
import sys
lines = int(input())
nums = []
for i in range(lines):
    num = int(sys.stdin.readline())
    nums.append(num)

nums.sort()
for j in nums:
    print(j)
    
    

## 기존 풀이
"""
lines = int(input())
nums = []
for i in range(lines):
    num = int(input())
    nums.append(num)

nums.sort()
for j in nums:
    print(j)
"""