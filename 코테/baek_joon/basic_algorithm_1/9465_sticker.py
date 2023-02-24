
''''
1 2 3 4 5
6 7 8 9 10
계산식을 구해보면

1,6 은 고정시키고
2,7은 2+6, 1+7중 큰수를 선택하는 것이다.
다음 3,8에서 3은 7선택까지의 합과 6을 선택했을 때의 값과
비교한다. 여기서 1을 선택하는 경우는 7을 선택하는 것에 포함
되어있기 때문에 제외한다.

'''
import sys
input = sys.stdin.readline
cnt=int(input())
for j in range(cnt):
    line = int(input())
    arr=[]
    
    
    # 2줄이니까 2번 반복
    for k in range(2):
        arr.append(list(map(int, input().split())))
        

    ## n이 1이면 위아래중 큰거 출력
    if line==1:
        print(max(arr[0][0],arr[1][0]))
        continue


    # 각각 2번째 값은 대각선끼리 더한 것으로 초기화
    arr[0][1] = arr[0][1]+arr[1][0]
    arr[1][1] = arr[1][1]+arr[0][0]

    if line==2:
        print(max(arr[0][-1],arr[1][-1]))
        continue

    for i in range(2, line):
        
        arr[0][i] = arr[0][i] + max(arr[1][i-1], arr[1][i-2])
        arr[1][i] = arr[1][i] + max(arr[0][i-1], arr[0][i-2])
        
    print(max(arr[0][-1],arr[1][-1]))