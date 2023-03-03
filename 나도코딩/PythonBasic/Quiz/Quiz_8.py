"""
Quiz)_주어진 코드를 활용하여 부동산 프로그램을 작성하시오

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    # 매물 초기화
    # def __init__(self, location, house_type 아파트 or 오피스텔, deal_type = 매매 or 전세
    # , price = 가격, completion_year = 준공연도):

    # 
    # 매물 정보 표시 -> 위 출력예제를 출력하는 함수
    # def show_detail(self)
    # pass"""

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type,\
             self.price, self.completion_year)
  

# house 객체를 만들어 정보 입력
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "50억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

# 일괄 관리를 위해 리스트로 정리
houses = []
houses.append(house1)
houses.append(house2)
houses.append(house3)

# 출력 부분
print("총 {0} 대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()

