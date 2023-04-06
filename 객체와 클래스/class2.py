
class Student:
    
    def __init__(self, id_num, age, gender, Score=0):
        self.id_num = id_num
        self.age = age
        self.gender = gender
        
    
    def UCheck(self, check):
        if check =="O":
            print("출석 완료")
        else:
            print("에러 발생. 위치를 확인하세요")


st1 = Student(101, 22, "남자")

