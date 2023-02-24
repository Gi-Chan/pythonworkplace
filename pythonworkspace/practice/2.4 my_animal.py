# 애완동물을 소개해 주세요~

hobby = "산책"
animal = "강아지"
name = "연탄이"
age = 4
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + " 입니다.")
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")

''' 문자열 및 변수에서 "+" 기호말고 ",(콤마)"를 쓸 경우 자동으로 띄어쓰기 1칸에
정수형 값을 문자열 변환(str) 처리를 하지 않아도 된다'''

print( name + "는 어른일까요? " + str(is_adult))