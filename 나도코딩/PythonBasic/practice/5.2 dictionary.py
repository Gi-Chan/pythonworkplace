# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))

# 키 값을 대괄호로 가져오면 키가 없을 경우 프로그램 종료
# get은 None 출력 후 계속 진행
# print(cabinet[5])
# print(cabinet.get(3))
# print("hi")

# get의 경우 None 대신에 출력 문장을 정할 수 있음
# print(cabinet.get(5, "사용 가능"))

# print(3 in cabinet) # 캐비넷 안에 키를 확인 하는 법. 있으면 True
# print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

# 새 손님
print(cabinet)
cabinet["C-20"] = "조세호" # C-20이라는 키를 만들고 값은 조세호를 넣음
print(cabinet)


# 간 손님
del cabinet["A-3"] # A-3 이라는 키 삭제
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 둘 다 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)