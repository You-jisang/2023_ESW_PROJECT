from Floor import Floor
from Background import Background

class Stage:
    def __init__(self, background_image_path, floor_image_path, floor_positions, 
                 obstacle_image_path, obstacles_positions, star_image_path, star_positions): #초기화 함수 정의
        self.background = Background(background_image_path, 13, 13) # 스테이지 배경 설정, 벽 두께 13, 바닥 두께 13
        # Floor 클래스의 인스턴스 생성
        # 각 발판의 이미지 경로, 위치, 크기(가로20 세로10, 상태번호 0)
        self.floors = [Floor(floor_image_path, pos, (20, 10), 0) for pos in floor_positions] 
        # 각 가시의 이미지 경로, 위치, 크기(가로20 세로10, 상태번호 1)
        self.obstacles = [Floor(obstacle_image_path, pos, (20, 10), 1) for pos in obstacles_positions] 
        # 각 별의 이미지 경로, 위치, 크기(가로20 세로19, 상태번호 2)
        self.stars = [Floor(star_image_path, pos, (20, 19), 2) for pos in star_positions] 

    def draw(self, canvas):
        self.background.draw(canvas)
        for obstacle in self.obstacles:
            obstacle.draw(canvas) # 가시 그리기
        for floor in self.floors:
            floor.draw(canvas) # 발판 그리기
        for star in self.stars:
            star.draw(canvas) # 별 그리기
        
    # 충돌 확인 후 동작 수행
    def check_collision(self, ball):
        for obstacle in self.obstacles:
            obstacle.check_collision(ball) 
        for floor in self.floors:
            floor.check_collision(ball)
        for star in self.stars:
            star.check_collision(ball)
        

        