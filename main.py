from Ball import Ball
from Background import Background
from Joystick import Joystick
from Stage import Stage
from PIL import Image

#dfsd
def process_input(joystick, ball, a_pressed):
    # Read joystick input and move the ball
    if joystick.button_A.value and a_pressed:
        a_pressed = False

    # 한번 A 누르면
    if not joystick.button_A.value and not a_pressed:
        if joystick.button_L.value == False or joystick.button_R.value == False:
            ball.dashjump()
        a_pressed = True

    if joystick.button_L.value == False:
        ball.acceleration[0] = -1
    elif joystick.button_R.value == False:
        ball.acceleration[0] = 1
    else:
        if ball.velocity[0] > 0:
            ball.acceleration[0] = -1
        else:
            ball.acceleration[0] = 1

def update_game_state(ball, background, stage):
    ball.move()
    background.check_collision(ball)
    stage.check_collision(ball)
    

def render_game_state(joystick, ball, background, stage):
    # Create a new canvas for each frame
    canvas = Image.new('RGB', (joystick.width, joystick.height), 'white')

    # Draw the background, then the bal1 1
    background.draw(canvas)
    stage.draw(canvas)
    ball.draw(canvas)

    # Show the canvas on the display
    joystick.disp.image(canvas)
    
def main():
    # Initialize game entities
    joystick = Joystick()
    ball = Ball(10, 150, 0, 10, 1, 1, 5)
    background = Background('/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/startback.png', 13, 13)

    canvas = Image.new('RGB', (joystick.width, joystick.height), 'white')

    start_path = "/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/startmain.png"
    start_image = Image.open(start_path)
    end_path = "/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/finish.png"
    end_image = Image.open(end_path)

    a_pressed = False

    start_scene = True

    stages = []

    stage_floor_positions = [(190, 208), (155, 188), (120, 169), (85, 150), (45, 150), (16, 126), (46, 101), (86, 101), (126, 101), (166, 101), (204, 101)]
    stage_obstacles_positions = [(65, 150), (106, 101), (146, 101)]
    stage_star_positions = [(204, 81)]
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
    
    stages.append(stage1)
    stages.append(stage2)
    stages.append(stage3)
    stages.append(stage4)
    stages.append(stage5)
    stages.append(null_stage)

    # Game loop
    while True:
        
        while start_scene:
            if not joystick.button_B.value:
                start_scene = False

            canvas.paste(start_image, (0, 0))
            joystick.disp.image(canvas)

        # 1. Process input
        process_input(joystick, ball, a_pressed)

        # 2. Update game state
        update_game_state(ball, background, stages[ball.stage_num])

        # 3. Render game state
        render_game_state(joystick, ball, background, stages[ball.stage_num])

        while(ball.stage_num == 5):
            canvas.paste(end_image, (0, 0))
            joystick.disp.image(canvas)


if __name__ == "__main__":
    main()