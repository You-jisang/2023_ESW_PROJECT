from PIL import Image
import numpy as np
from Joystick import Joystick

joystick = Joystick()
class Ball:
    def __init__(self, x, y, vx, vy, ax, ay, max_x_velo):
        self.image = Image.open('/home/youjisang/ESW-PROJECT/2023_ESW_PROJECT/images/capKirby.png')
        self.image = self.image.resize((20, 20), Image.LANCZOS)
        self.max_vx = max_x_velo
        self.position = np.array([x, y], dtype=float)
        self.velocity = np.array([vx, vy], dtype=float)  # vy 값을 변경하면 공이 튀어오르는 속도를 조절할 수 있습니다.
        self.acceleration = np.array([ax, ay], dtype=float)  # ay 값을 변경하면 공이 떨어지는 속도를 조절할 수 있습니다.

    def move(self):
        # 조이스틱 양 옆이 눌렸을 때
        if (joystick.button_L.value == False) or (joystick.button_R.value == False):
            self.position[0] += self.velocity[0]
            if self.acceleration[0] * self.velocity[0] < self.max_vx:
                self.velocity[0] += self.acceleration[0]
        else:
            #속도가 0이 될때까지
            if self.velocity[0] != 0:
                self.position[0] += self.velocity[0]
                self.velocity[0] += self.acceleration[0]
            

        self.position[1] += self.velocity[1]
        self.velocity[1] += self.acceleration[1]
    

    def draw(self, canvas):
        canvas.paste(self.image, tuple(map(int, self.position)), self.image)