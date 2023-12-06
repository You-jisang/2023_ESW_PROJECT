from Ball import Ball
from Background import Background
from Joystick import Joystick
from Stage import Stage
from PIL import Image

#dfsd
def process_input(joystick, ball):
    # Read joystick input and move the ball
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
    background = Background('/home/youjisang/ESW-PROJECT/2023_ESW_PROJECT/images/startback.png', 10, 13)

    stage1_floor_positions = [(0, 0)]
    stage1 = Stage('/home/youjisang/ESW-PROJECT/2023_ESW_PROJECT/images/startback.png', 
                   '/home/youjisang/ESW-PROJECT/2023_ESW_PROJECT/images/floor.png',
                   stage1_floor_positions)
    
    # Game loop
    while True:
        
        # 1. Process input
        process_input(joystick, ball)

        # 2. Update game state
        update_game_state(ball, background, stage1)

        # 3. Render game state
        render_game_state(joystick, ball, background, stage1)

if __name__ == "__main__":
    main()