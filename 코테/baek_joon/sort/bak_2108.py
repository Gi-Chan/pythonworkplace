import sys
from collections import Counter
n = int(sys.stdin.readline())
if n%2==0 or n>500000: ## 짝수면 에러발생
    raise ValueError
arr =[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
## 산술평균
print(round(sum(arr)/n))

## 중앙 값
arr2 = sorted(arr)
print(arr2[n//2])

## 최빈값
## Counter 라이브러리를 사용하면 가장 자주 나오는 숫자를 알 수 있음
# most_common(0)은 처음, n이면 n+1번째 많이 나오는 숫자
cnt = Counter(arr).most_common()
if len(cnt) == 1:
    print(cnt[0][0])
elif cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
## 범위 : 최댓값과 최솟값의 차이
print(max(arr)-min(arr))

## https://joylee-developer.tistory.com/94 이거 보셈