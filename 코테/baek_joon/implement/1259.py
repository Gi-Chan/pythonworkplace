
while True:
    num=int(input())
    if num == 0:
        break
    else:
        num = list(str(num)) # 123 입력하면 ['1', '2', '3'] 로 바꿔줌
        
    num2=list(reversed(num)) # num2에 num을 뒤집은 값을 넣음
    if num == num2:
        print('yes')
    else:
        print('no')
    




    