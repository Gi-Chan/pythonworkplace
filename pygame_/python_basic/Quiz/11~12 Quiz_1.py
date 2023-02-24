"""Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS 는 30 으로 고정

[게임 이미지]
1. 배경 : 640 * 480 (세로 가로) - background.png
2. 캐릭터 : 70 * 70 - character.png
3. 똥 : 70 * 70 - enemy.png """

import pygame
from random import *
###################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# FPS
clock = pygame.time.Clock()
###################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 화면
background = pygame.image.load("C:/python/python_usage1.py/Quiz/background.png")

# 3. 게임 캐릭터 위치 정의
character = pygame.image.load("C:/python/python_usage1.py/Quiz/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width - character_width ) / 2 
character_y_pos = screen_height - character_height  

# 이동 위치
character_to_x = 0
character_speed = 10


# 적 캐릭터
enemy = pygame.image.load("C:/python/python_usage1.py/Quiz/enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = randrange(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 시작 시간
start_ticks = pygame.time.get_ticks()



running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                character_to_x += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x
    

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width    

    # 똥 위치 정의
    enemy_y_pos += enemy_speed
    if enemy_y_pos >= screen_height:
        enemy_x_pos = randrange(0, screen_width - enemy_width)
        enemy_y_pos = 0


    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌햇어요 버틴 시간은 {0} 초".format(int(elapsed_time)))
        running = False

    # 5. 화면에 그리기
    # 배경 그리기
    screen.blit(background, (0, 0))

    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # 적 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 게임 시간
    elapsed_time = (pygame.time.get_ticks() + start_ticks) / 1000 - 2
    # 시간
    timer = game_font.render(str(int(elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))


    pygame.display.update()

pygame.quit()