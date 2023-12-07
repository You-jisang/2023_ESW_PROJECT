from PIL import Image
import numpy as np
from Joystick import Joystick

joystick = Joystick()
class Ball:
    def __init__(self, x, y, vx, vy, ax, ay, max_x_velo):
        self.image = Image.open('/home/youjisang/ESW_PROJECT/2023_ESW_PROJECT/images/kirby.png') # 커비 이미지 오픈 후 저장
        self.image = self.image.resize((20, 20), Image.LANCZOS) # 20x20사이즈로 변경
        self.max_vx = max_x_velo # 커비의 최대 x축 속도 설정
        self.position = np.array([x, y], dtype=float) # 커비의 초기 위치 설정
        self.velocity = np.array([vx, vy], dtype=float)  # vy 값을 변경해 공이 튀어오르는 속도를 조절(초기속도)
        self.acceleration = np.array([ax, ay], dtype=float)  # ay 값 변경해 공이 떨어지는 속도를 조절(가속도)
        self.dash_chance = 1 # 대쉬 찬스 1회
        self.stage_num = 0 # 스테이지 번호 0

    def move(self):
        # 조이스틱 양 옆이 눌렸을 때
        # 커비의 x축 위치를 속도만큼 변경, 속도를 가속도만큼 변경
        if (joystick.button_L.value == False) or (joystick.button_R.value == False):
            self.position[0] += self.velocity[0]
            if self.acceleration[0] * self.velocity[0] < self.max_vx:
                self.velocity[0] += self.acceleration[0]
            # 속도가 최대 속도를 초과하지 않게 설정
            elif self.acceleration[0] * self.velocity[0] > self.max_vx:
                self.velocity[0] -= self.acceleration[0]
            
        else:
            #속도가 0이 될때까지
            if self.velocity[0] != 0:
                self.position[0] += self.velocity[0]
                self.velocity[0] += self.acceleration[0]
            
        # 커비의 y축 위치를 속도만큼 변경하고, 속도를 가속도만큼 변경
        self.position[1] += self.velocity[1]
        self.velocity[1] += self.acceleration[1]
    

    def draw(self, canvas):
        canvas.paste(self.image, tuple(map(int, self.position)), self.image)

    # 대쉬 기능 구현
    def dashjump(self):
        if self.dash_chance == 1:
            self.dash_chance -= 1
            self.velocity[1] = -4 # 커비의 y축 속도 조절
            self.velocity[0] = (self.acceleration[0] / abs(self.acceleration[0])) * 10 # 커비의 x축 속도 조절, 절대값으로 좌우 둘다 가능