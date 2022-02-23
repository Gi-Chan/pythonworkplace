python = "Python is Amazing"
print(python.lower()) # 해당 변수에 대문자를 소문자로 변환
print(python.upper()) # 해당 변수에 소문자를 소문자로 변환
print(python[0].isupper()) # python 문자열 []번째 값이 대문자면 True 
print(len(python))  # pyhon 전체 문자열의 길이 반환

# python.repalce("A", "B") : python 문자열에 있는 A를 찾아서 B로 바꾸는 함수
print(python.replace("Python", "Java")) 

# pythopn.index("?") : python 문자열 안에 ?가 첫 번째로 나오는 인덱스 출력
index = python.index("n")
print(index)

# 문자열중 ?가 두번째 나오는 인덱스 출력
index = python.index("n", index + 1)
print(index)

# python.find("?") : 문자열 안에서 ?의 인덱스 출력 없을 경우 -1 출력
print(python.find("n")) 

# python이라는 문자열에 java가 없으면 에러발생.. 
# print(python.index("Java"))
# *find는 프로그램이 진행되지만 index는 에러가 나오며 종류됨에 유의*

# python.count("?") 문자열에 ?가 몇 개 있는지 출력
print(python.count("n"))