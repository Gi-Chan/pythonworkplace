"""Quiz)_동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오

조건1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
        출력 메시지: "잘못된 값을 입력하였습니다.
조건2: 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소진 시 사용자 정의 에러[SoldOutEroor]를 발생시키고 프로그램 종료
        출력 메시지: "재고가 소진되어 더 이상 주무을 받지 않습니다."""

# 사용자 에러
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

# 초기 값
chicken = 10 # 치킨 재고량
waiting = 1 # 대기번호 1부터

# 주문 받는 곳

while(True):

    try:
        
        print("남은 치킨 {0}마리".format(chicken))
        order = int(input("몇 마리 주문하시겠습니까? : "))

        if order > chicken: # 주문량이 재고보다 많을 경우
                print("죄송합니다. 재고가 부족해서 {0}마리 이하로 주문해주세요.".format(chicken))
        
        elif order <= 0: # 주문량이 1마리 미만일 경우
            raise ValueError
        
        else: # 주문 완료
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(\
            waiting, order))
            chicken -= order
            waiting += 1

        if chicken == 0: # 남은 치킨량이 0이면 종료
                raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")

    except ValueError:
            print("잘못된 값을 입력하였습니다.")
    except SoldOutError as err:
        print(err)
        break
        

