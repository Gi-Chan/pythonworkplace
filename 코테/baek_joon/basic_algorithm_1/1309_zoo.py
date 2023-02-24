

'''
가로는 2 고정이고 세로가 늘어난다.
가로는 선택을 안한경우, 왼쪽 선택, 오른쪽 선택 총 3가지 경우가 존재함
dp 2차원으로 해결하자

'''

# line=4
line = int(input())
mod = 9901
arr = [ [0 for i in range(3)] for i in range(line+1)]
# arr[1][1,2,3] 여기서 1,2,3은 선택x, 왼쪽, 오른쪽
arr[1][0] = 1
arr[1][1] = 1
arr[1][2] = 1

for i in range(2, line+1):
    arr[i][0] = (arr[i-1][0] + arr[i-1][1] + arr[i-1][2]) % mod
    arr[i][1] = (arr[i-1][0] + arr[i-1][2]) % mod
    arr[i][2] = (arr[i-1][0] + arr[i-1][1]) % mod

print(sum(arr[line])%mod)