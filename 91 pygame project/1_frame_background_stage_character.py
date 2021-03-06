import os
import pygame
#################################################################
# 기본 초기화 (반드시 해야 하는 것들)
#
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang") # 게임 이름

# FPS (Frame per second)
clock = pygame.time.Clock()
#
#################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게입 이미지 , 좌표, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 화일 위치를 반환
image_path = os.path.join(current_path, "images") # image folder 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# stage 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # stage의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height) - (character_height) - stage_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 10

###########################################################
#
###########################################################

running = True # 게임이 진행중인가?
while running:
  dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

  # 2. 이벤트 처리 (키보드, 마우스 등)
  for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
    if event.type == pygame.QUIT: # 게임창이 닫히는 이반트인가?
      running = False # 게임이 진행중이 아님

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
        character_to_x -= character_speed
      elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
        character_to_x += character_speed
      elif event.key == pygame.K_SPACE: # 무기 발사
        pass

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        character_to_x = 0


  # 3. 게임 캐릭터 위치 정의
  character_x_pos += character_to_x

  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width:
    character_x_pos = screen_width - character_width


  # 4. 충돌 처리

  # 5. 화면에 그리기
  screen.blit(background, (0, 0))
  screen.blit(stage, (0, (screen_height - stage_height)))
  screen.blit(character, (character_x_pos, character_y_pos))

  pygame.display.update() # 게임화면을 다시 그리기


# pygame 종료
pygame.quit()