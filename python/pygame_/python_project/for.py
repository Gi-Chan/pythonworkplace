balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

for ball_idx, ball_val in enumerate(balls):
    print("\nball :", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons :", weapon_val)
        if ball_val == weapon_val: # 충돌 체크
            print("공과 무기가 충돌")
            # break
    else: # for 에도 else가 가능하고 이 else는 더 이상 for 반복을 할 수 없을 때 진행됨.
        continue
    print("바깥 for 문 break")
    break




"""
    for 바깥조건:
        바깥동작
        for 안쪽조건:
            안쪽동작
            if 충돌하면:
                break
            
        else:
            cotinue
        break
    
    """