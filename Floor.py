from PIL import Image
import numpy as np

class Floor:
    def __init__(self, image_path, position, size, num = 0): # 이미지 경로, 위치, 크기, 상태번호 (Stage에서 사용됨)
        self.image = Image.open(image_path) # 이미지 오픈 및 저장
        self.position = position
        self.size = size
        self.state = 'floor' # 초기 상태(0)를 floor로 설정
        if (num == 1):
            self.state = 'obstacle' # 상태번호가 1일 경우 obstacle(가시)로 설정
        elif (num == 2):
            self.state = 'star'  # 상태번호가 2일 경우 star(별)로 설정
        
        if num == 1: # 가시 장애물의 충돌 범위 조절을 위해 설정, 좌우 5씩 조정 -> 발판과 중복 충돌을 방지하기 위해서 
            self.pos = np.array([self.position[0] + 5, self.position[1], self.position[0] + self.size[0] - 5, self.position[1] + self.size[1]])
        else: # 그렇지 않을 경우 그대로 사용
            self.pos = np.array([self.position[0], self.position[1], self.position[0] + self.size[0], self.position[1] + self.size[1]])
        

    def draw(self, canvas):
        canvas.paste(self.image, self.position, self.image) # 마지막에 self.image를 해줌으로써 배경 투명화 적용

    def get_bounding_box(self):
        return (self.position[0], self.position[1], self.position[0] + self.size[0], self.position[1] + self.size[1])

    def check_collision(self, ball):
        # 커비 이미지가 20x20 이므로 좌상단과 우하단 모서리 좌표 입력
        ball_pos = np.array([ball.position[0], ball.position[1], ball.position[0] + 20, ball.position[1] + 20])
        
        # 커비와 발판, 가시, 별과 겹치는지 확인
        collision = self.overlap(ball_pos, self.pos)

        # 커비가 아래로 떨어지고 있고, 커비의 하단과 바운딩 박스의 상단이 만나 발판 위로 움직이는 지 확인 
        if collision and ball_pos[3] <= self.pos[1] + ball.velocity[1] and ball.velocity[1] >= 0:
            if self.state == 'obstacle':
                print("가시")
                ball.position = np.array([25, 200], dtype=float) # 상태번호 1일 경우 초기 위치로 커비 이동
            elif self.state == 'floor':
                ball.position[1] = self.position[1] - 20
                ball.velocity[1] = -6.5 # 높이 튀어오르는 정도
                ball.dash_chance = 1 # 대쉬 찬스 초기화
            elif self.state == 'star':
                print("별")
                ball.position = np.array([25, 200], dtype=float)
                ball.stage_num += 1 # 별을 먹을 경우 초기위치로 이동하고 스테이지 이동



    # 두 사각형(발판, 가시)가 겹치는 지 확인
    def overlap(self, rect1, rect2): 
        return not (rect1[2] < rect2[0] or rect1[0] > rect2[2] or rect1[1] > rect2[3] or rect1[3] < rect2[1])
    