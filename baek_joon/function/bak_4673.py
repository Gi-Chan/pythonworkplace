
a=0
ran = []
cnt = 1
while cnt<=10000:
    a +=1 # 원래 숫자
    sum=a # a에 각 자리수를 더한 값을 넣는 값
    nums = [] # 분리한 숫자
    
    ## 원래 숫자를 각 자리수로 나누어 리스트로 저장
    for i in map(int, str(a)):
        nums.append(i)
    
    ## 각 자리수로 나눈 값을 더함
    for j in nums:
        sum += j
     

    ## 생성자를 배열에 넣기
    ran.append(sum)

    cnt +=1


for k in range(1, 10001):
    if k not in ran:
        print(k)


