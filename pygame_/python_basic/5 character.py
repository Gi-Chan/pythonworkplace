import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/python/python_usage1.py/background.png")

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load("C:/python/python_usage1.py/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기

# 캐릭터가 화면 절반크기에 위치하는 데 캐릭터의 크기의 절반만큼을 빼야 중앙에 위치함.
character_x_pos = (screen_width - character_width ) / 2 

# 화면 세로 크기 가장 아래에 캐릭터 위치후 캐릭터의 높이를 빼주면 정상적으로 위치함.
character_y_pos = screen_height - character_height  

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()