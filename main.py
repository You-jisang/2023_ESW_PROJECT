from Ball import Ball
from Background import Background
from Joystick import Joystick
from Stage import Stage
from PIL import Image


def process_input(joystick, ball, a_pressed):
    # A 버튼 상태 확인
    if joystick.button_A.value and a_pressed:
        a_pressed = False

    # 좌우이동 하고 있을 때만 대쉬 점프 가능
    if not joystick.button_A.value and not a_pressed:
        if joystick.button_L.value == False or joystick.button_R.value == False:
            ball.dashjump()
        a_pressed = True

    # 볼 방향 전환, 가속도 1(-1) 설정
    if joystick.button_L.value == False:
        ball.acceleration[0] = -1
    elif joystick.button_R.value == False:
        ball.acceleration[0] = 1
    else:
        if ball.velocity[0] > 0:
            ball.acceleration[0] = -1
        else:
            ball.acceleration[0] = 1

# 게임 상태 업데이트
def update_game_state(ball, background, stage):
    ball.move() # 볼 움직이기
    # 배경과 스테이지의 충돌 검사 수행
    background.check_collision(ball) 
    stage.check_collision(ball)
    
# 게임 상태를 랜더링
def render_game_state(joystick, ball, background, stage):
    # 캔버스 생성
    canvas = Image.new('RGB', (joystick.width, joystick.height), 'white')

    # 캔버스에 배경, 스테이지, 볼 그림
    background.draw(canvas)
    stage.draw(canvas)
    ball.draw(canvas)

    # 조이스틱의 디스플레이에 캔버스 출력
    joystick.disp.image(canvas)
    
def main():
    joystick = Joystick()
    # 위치, 속도, 가속도 (x,y, vx, vy, ax, ay, max_x_velo)
    ball = Ball(10, 150, 0, 10, 1, 1, 5)
    # 배경의 벽, 바닥 두께 설정
    background = Background('/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/startback.png', 13, 13)

    canvas = Image.new('RGB', (joystick.width, joystick.height), 'white')

    # 게임 시작 화면
    start_path = "/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/startmain.png"
    start_image = Image.open(start_path)
    # 클리어 화면
    end_path = "/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/finish.png"
    end_image = Image.open(end_path)

    # A버튼 상태 확인
    a_pressed = False

    # 게임 시작 화면 표시 결정
    start_scene = True

    # 게임 스테이지 저장
    stages = []

    # 바닥 이미지 좌측 상단 좌표(바닥 그리기)
    stage_floor_positions = [(190, 208), (155, 188), (120, 169), (85, 150), (45, 150), (16, 126), (46, 101), (86, 101), (126, 101), (166, 101), (204, 101)]
    # 가시 이미지 좌측 상단 좌표(가시 그리기)
    stage_obstacles_positions = [(65, 150), (106, 101), (146, 101)]
    # 별 이미지 좌측 상단 좌표(별 그리기)
    stage_star_positions = [(204, 81)]
    # 스테이지 1 생성
    stage1 = Stage('/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/startback.png', 
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/floor.png',
                   stage_floor_positions,
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/obstacle.png',
                   stage_obstacles_positions,
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/star.png',
                   stage_star_positions
                   )
    
    stage_floor_positions = [(189, 199), (154, 180), (120, 159), (25, 158), (47, 133), (79, 114), (159, 114), (206, 114)]
    stage_obstacles_positions = [(99, 114), (119, 114), (139, 114)]
    stage_star_positions = [(206, 94)]
    stage2 = Stage('/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/startback.png',
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/floor.png',
                   stage_floor_positions,
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/obstacle.png',
                   stage_obstacles_positions,
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/star.png',
                   stage_star_positions
                   )
    
    stage_floor_positions = [(189, 199), (117, 181), (189, 158), (117, 134), (189, 114), (117, 91), (57, 91), (17, 91)]
    stage_obstacles_positions = [(37, 91), (77, 91), (97, 91)]
    stage_star_positions = [(17, 74)]
    stage3 = Stage('/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/startback.png',
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/floor.png',
                   stage_floor_positions,
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/obstacle.png',
                   stage_obstacles_positions,
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/star.png',
                   stage_star_positions
                   )
    
    stage_floor_positions = [(41, 202), (141, 202), (26, 145), (77, 145), (125, 145), (51, 125), (82, 105), (113, 85), (174, 145), (202, 165), (174, 185)]
    stage_obstacles_positions = [(61, 202), (81, 202), (101, 202), (121, 202), (81, 168), (101, 168), (121, 168), (141, 168)]
    stage_star_positions = [(113, 65)]
    stage4 = Stage('/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/startback.png',
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/floor.png',
                   stage_floor_positions,
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/obstacle.png',
                   stage_obstacles_positions,
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/star.png',
                   stage_star_positions
                   )
    
    stage_floor_positions = [(45, 200), (45, 152), (45, 104), (45, 56), (45, 32), (19, 32), (19, 80), (19, 128), (19, 176)]
    stage_obstacles_positions = [(65, 217), (85, 217), (105, 217), (125, 217), (145, 217), (165, 217), (185, 217), (65, 203),
                                 (65, 189), (65, 175), (65, 161), (65, 147), (65, 133), (65, 119), (65, 91), (65, 77), (65, 63),
                                 (65, 49), (85, 147), (105, 147), (125, 147), (145, 147), (165, 147), (125, 77), (145, 77), (165, 77), (185, 77), (205, 77)]
    stage_star_positions = [(206, 208)]
    stage5 = Stage('/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/startback.png',
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/floor.png',
                   stage_floor_positions,
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/obstacle.png',
                   stage_obstacles_positions,
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/star.png',
                   stage_star_positions
                   )
    
    # 더미 스테이지
    stage_floor_positions = [(45, 200), (45, 152), (45, 104), (45, 56), (45, 32), (19, 32), (19, 80), (19, 128), (19, 176)]
    stage_obstacles_positions = [(65, 217), (85, 217), (105, 217), (125, 217), (145, 217), (165, 217), (185, 217), (65, 203),
                                 (65, 189), (65, 175), (65, 161), (65, 147), (65, 133), (65, 119), (65, 91), (65, 77), (65, 63),
                                 (65, 49), (85, 147), (105, 147), (125, 147), (145, 147), (165, 147), (125, 77), (145, 77), (165, 77), (185, 77), (205, 77)]
    stage_star_positions = [(206, 208)]
    null_stage = Stage('/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/startback.png',
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/floor.png',
                   stage_floor_positions,
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/obstacle.png',
                   stage_obstacles_positions,
                   '/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/star.png',
                   stage_star_positions
                   )
    
    # 생성한 스테이지 stages 리스트에 추가
    stages.append(stage1)
    stages.append(stage2)
    stages.append(stage3)
    stages.append(stage4)
    stages.append(stage5)
    # 클리어 화면을 위해 더미 스테이지 추가
    stages.append(null_stage)

    # 게임 루프
    while True:
        # B버튼 누르면 게임 시작
        while start_scene:
            if not joystick.button_B.value:
                start_scene = False

            canvas.paste(start_image, (0, 0))
            joystick.disp.image(canvas)

        # 사용자 입력 처리
        process_input(joystick, ball, a_pressed)

        # 게임 상태 업데이트
        update_game_state(ball, background, stages[ball.stage_num])

        # 게임 상태 랜더링
        render_game_state(joystick, ball, background, stages[ball.stage_num])

        # 스테이지가 더미 스테이지로 이동했을 경우 클리어 화면 출력
        while(ball.stage_num == 5):
            canvas.paste(end_image, (0, 0))
            joystick.disp.image(canvas)


if __name__ == "__main__":
    main()