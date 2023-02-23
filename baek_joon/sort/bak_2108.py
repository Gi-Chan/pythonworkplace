import sys
n = int(sys.stdin.readline())
if n%2==0 or n>500000: ## 짝수면 에러발생
    raise ValueError
arr =[]
for i in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)

## 산술평균
print(round(sum(arr)/n))

## 중앙 값
arr2 = []
arr2 = sorted(arr)
print(arr2[n//2])

## 최빈값

arr3={}
for i in range(n):
    if(arr[i] in arr3):
        arr3[arr[i]] += 1
    else:
        arr3[arr[i]]=1

print(max(arr3.keys()))


## 범위 : 최댓값과 최솟값의 차이
print(max(arr)-min(arr))