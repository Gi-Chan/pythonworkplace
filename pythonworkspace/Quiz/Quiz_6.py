"""Quiz)_표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(키) x 22
여자 : 키(m) x 키(키) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)

조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다."""

def std_weight(height, gender): # 표준 체중을 구하는 함수
    
    if gender == "남자":
        return height * height * 22
    
    elif gender == "여자":
        return height * height * 21
    
    else: # 성별에 다른값을 입력했을경우
        print("성별이 잘못 입력되었습니다.")
        exit() # 강제종료
    


height = int(input("키를 입력하세요(cm) : ")) / 100 # cm를 m로 변환
gender = input("성별을 입력하세요 : ")

weight = std_weight(height, gender)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(int(height * 100), gender, round(weight, 2)))


