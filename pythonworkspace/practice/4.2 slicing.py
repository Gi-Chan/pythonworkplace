jumin = "981002-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 인덱스 시작의 값이 처음일때는 0 생략가능
print("뒤 7자리 : " + jumin[7:]) # 인덱스 마지막의 값이 끝일때는 생략가능
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지