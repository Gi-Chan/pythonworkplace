num=-13
flag = 1
sign = [-1,1]
exp=0
two=2
result=0
while True:
    
    result += (two**exp) * sign[flag]

    exp+=1
    print(result)
    if num == result:
        print(result)
        break
    
    
    
    # -1 1 바궈주는거
    if flag==1:
        flag=0
    elif flag ==0:
        flag=1