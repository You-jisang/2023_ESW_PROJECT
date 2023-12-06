from Floor import Floor
from Background import Background

#!dfs
class Stage:
    def __init__(self, background_image_path, floor_image_path, floor_positions, obstacle_image_path, obstacles_positions, star_image_path, star_positions):
        self.background = Background(background_image_path, 10, 13)
        self.floors = [Floor(floor_image_path, pos, (20, 10), 0) for pos in floor_positions]
        self.obstacles = [Floor(obstacle_image_path, pos, (20, 10), 1) for pos in obstacles_positions]
        self.stars = [Floor(star_image_path, pos, (20, 19), 2) for pos in star_positions]

    def draw(self, canvas):
        self.background.draw(canvas)
        for obstacle in self.obstacles:
            obstacle.draw(canvas)
        for floor in self.floors:
            floor.draw(canvas)
        for star in self.stars:
            star.draw(canvas)
        

    def check_collision(self, ball):
        for obstacle in self.obstacles:
            obstacle.check_collision(ball)
        for floor in self.floors:
            floor.check_collision(ball)
        for star in self.stars:
            star.check_collision(ball)
        

        