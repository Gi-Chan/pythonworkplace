import theater_module

# theater_module.price(3) # 3명이서 영화 보러 갔을 떄 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# import theater_module as mv # 모듈이름을 mv로 간편하게 쓰기
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# from random import * 이런거 그냥 함수명만 적어도 사용가능
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning # 필요한 함수만 호출가능
# price(5)
# price_morning(6)
# price_soldier(4) # 호출을 안했기에 사용 불가

from theater_module import price_soldier as price
# ㄴ price_soldier 함수만 호출하는데 거기서 이름을 price라고 쓰고 싶음. 원래 price와 다른기능
price(5)