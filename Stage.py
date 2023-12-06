from Floor import Floor
from Background import Background

#!dfs
class Stage:
    def __init__(self, background_image_path, floor_image_path, floor_positions):
        self.background = Background(background_image_path, 10, 13)
        self.floors = [Floor(floor_image_path, pos, (20, 10)) for pos in floor_positions]

    def draw(self, canvas):
        self.background.draw(canvas)
        for floor in self.floors:
            floor.draw(canvas)

    def check_collision(self, ball):
        for floor in self.floors:
            floor.check_collision(ball)

        