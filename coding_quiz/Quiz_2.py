# 행맨 퀴즈 프로그램 만들기
from random import *

words = ["apple", "banana", "orange"]
word = choice(words)
print("answer : " + word)
letters = "" # 사용자로 부터 지금까지 입력받은 모든 알파벳

while True:
    succeed = True

    for w in word: 
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()

    if succeed:
        print("Succeed")
        break

    letter = input("글자를 입력하세요 : ")
    if letter not in letters:
        letters += letter

    if letter in word:
        print("Correct")
    else:
        print("Wrong")

    if letters == word:
        break