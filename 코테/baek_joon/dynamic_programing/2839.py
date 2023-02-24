n=int(input())
result=0

while n>=0: # 설탕이 0 이상일 때까지 작동
    if n%5==0: # 남은 설탕이 5로 나누어 떨어지면
        result += (n//5) # 결과값에 n/5의 몫을 더해줌
        print(result)
        break
    n-=3 # 남은 설탕이 5로 나누어 떨어지지 않으면 3만큼 빼고
    result+=1 # 결과값 1 추가
else: # while문이 거짓일 때 else문이 작동한다는 걸 새로 알음
    print(-1)
    

    
    
