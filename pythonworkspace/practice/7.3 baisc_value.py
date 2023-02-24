# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 언어 : {2}" \
#         .format(name, age, main_lang) )

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")


# 같은 학교, 학년, 반, 수업일 경우 기본값

# 기본값 할당 방법 age=17 처럼 함수내에서 정의
# 함추 호출시 입력값이 없을 경우 기본값 출력
def profile(name, age=17, main_lang ="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 언어 : {2}" \
        .format(name, age, main_lang) )

profile("유재석")
profile("김태호")