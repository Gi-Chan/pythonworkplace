n = int(input())

start = 666 # 시작 넘버는 666
cnt=0 # 666이 있는 숫자 체크
while True: # 무한반복으로 한다
    
    if '666' in str(start): # 숫자에 666이 있으면
        cnt+=1  # 카운트 증가
    
    if cnt == n: # 찾은 숫자 개수가 n과 같다면
        print(start) # 해당 숫자를 출력하고 반복문 종료
        break
    start+=1 # 숫자를 계속 증가시켜 모든 구간을 탐색한다