def profile(name, age, main_lang):
    print(name, age, main_lang)

# 함수에서 호출되는 값은 name=""이런식으로 키워드로 정리하면 정리한대로 넘어감
profile(name="유재석", main_lang="파이썬", age=25)
profile(name="김태호", age=25, main_lang="자바")
