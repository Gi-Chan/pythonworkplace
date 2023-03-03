# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")
# 할 줄 아는 언어가 늘어나거나 언어를 2개밖에 못하는 상황이면 매번 함수를 바꾸거나
# ""로 빈칸을 만들어야하는 불편함 발생!


# 인자를 *로 정의할 경우 입력값들이 자유자재로 늘었다 줄었다 함
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "javaScript")
profile("김태호", 25, "Kotlin", "Swift") 