# Quiz) "사회적 거리두기"에 따른 영화관 좌석 예매 시스템을 만드시오

# - 각 열은 1 ~ 20 번까지 총 20개의 좌석으로 구성
#  (예) A1 A2 A3 A4 ... A20
#       B1 B2 B3 B4 ... B20
#       C1 C2 C3 C4 ... C20

# - 이 때 A 열에 대해서 홀수로 끝나는 좌석에 대해서만 출력 (각 좌석은 " " 로 구분)
#  (예) A1 A3 A5 A7 ... A19


for i in range(1, 21): # A열 1 ~ 20까지 만들기
   if i % 2 == 1:
       print("A" + str(i), end=" ")


for i in range(1, 21)[::2]: # 2 칸씩 건너 뛰어서
    print("A" + str(i), end=" ")
