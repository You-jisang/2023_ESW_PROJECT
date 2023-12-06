from PIL import Image

class Background:
    def __init__(self, image_path, wall_thickness, floor_thickness):
        self.image = Image.open(image_path)
        self.wall_thickness = wall_thickness
        self.floor_thickness = floor_thickness
        self.width, self.height = self.image.size

    def draw(self, canvas):
        canvas.paste(self.image, (0, 0))

    def check_collision(self, ball):
        # 왼쪽 벽 또는 오른쪽 벽과의 충돌 검사
        if ball.position[0] < self.wall_thickness:  # 공이 왼쪽 벽을 통과하려 하면
            ball.position[0] = self.wall_thickness  # 왼쪽 벽에 공을 고정시킴
            ball.velocity[0] *= -1  # 벽과 충돌하면 x축 방향 속도를 반대로 바꿔줌
        elif ball.position[0] + ball.image.width > self.width - self.wall_thickness:  # 공이 오른쪽 벽을 통과하려 하면
            ball.position[0] = self.width - self.wall_thickness - ball.image.width  # 오른쪽 벽에 공을 고정시킴
            ball.velocity[0] *= -1  # 벽과 충돌하면 x축 방향 속도를 반대로 바꿔줌
        # 바닥과의 충돌 검사
        if ball.position[1] + ball.image.height >= self.height - self.floor_thickness:
            ball.velocity[1] = -8 # 벽과 충돌하면 y축 방향 속도를 반대로 바꿔줌

        return None
