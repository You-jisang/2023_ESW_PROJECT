from PIL import Image
import numpy as np

class Floor:
    def __init__(self, image_path, position, size, num = 0):
        self.image = Image.open(image_path)
        self.position = position
        self.size = size
        self.state = 'floor'
        if (num == 1):
            self.state = 'obstacle'
        elif (num == 2):
            self.state = 'star'
        
        if num == 1:
            self.pos = np.array([self.position[0] + 5, self.position[1], self.position[0] + self.size[0] - 5, self.position[1] + self.size[1]])
        else:
            self.pos = np.array([self.position[0], self.position[1], self.position[0] + self.size[0], self.position[1] + self.size[1]])
        

    def draw(self, canvas):
        canvas.paste(self.image, self.position, self.image)

    def get_bounding_box(self):
        return (self.position[0], self.position[1], self.position[0] + self.size[0], self.position[1] + self.size[1])

    def check_collision(self, ball):

        ball_pos = np.array([ball.position[0], ball.position[1], ball.position[0] + 20, ball.position[1] + 20])
        
        collision = self.overlap(ball_pos, self.pos)

        if collision and ball_pos[3] <= self.pos[1] + ball.velocity[1] and ball.velocity[1] >= 0:
            if self.state == 'obstacle':
                print("가시")
                ball.position = np.array([25, 200], dtype=float)
            elif self.state == 'floor':
                ball.position[1] = self.position[1] - 20
                ball.velocity[1] = -6.5
                ball.dash_chance = 1
            elif self.state == 'star':
                print("별")
                ball.position = np.array([25, 200], dtype=float)
                ball.stage_num += 1




    def overlap(self, rect1, rect2):
        return not (rect1[2] < rect2[0] or rect1[0] > rect2[2] or rect1[1] > rect2[3] or rect1[3] < rect2[1])
    