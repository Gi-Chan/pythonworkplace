
arr =[8,20,42,0]
flag = True
'''
일단 소수를 다 구하고
주어진 소수 이하부터 비교를함

주어진 숫자 미만 의 소수 a[i] (i=0부터):
    if num == a[i]+a[j] (j는 i+1부터 1씩 증가함)
        flag = true
        break
    else:
        not
'''
# 소수 구하기
def is_sosu(x):
    # x의 제곱근이 있다면 소수가 아니므로 (ex 9 = 3*3)
    # 탐색범위를 sqrt(x)까지 한다.
    for j in range(2,int((x**0.5))+1):
        if x%j==0:
            return False
    return True

## 더한 값이 결과랑 같은지 비교
def find_sosu(size):
    
    for i in range(size):
        
        for j in range(i,size):
            if sosu[i]+sosu[j] == result:
                return True, i, j
    return False


for i in range(len(arr)-1):
    
    result = arr[i]
    sosu = []
    # 소수 구하기
    for i in range(result+1):
        if i==1 or i==2:
            continue
        if is_sosu(i):
            sosu.append(i)
    size = len(sosu)
    
    nums = find_sosu(size)
    
    if nums[0]:
        num1 = sosu[nums[1]]
        num2 = sosu[nums[2]]
       
    
    
    print("{} = {} + {}".format(result, num1, num2))