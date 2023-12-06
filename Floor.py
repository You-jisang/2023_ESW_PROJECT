from PIL import Image
#sd
class Floor:
    def __init__(self, image_path, position, size):
        self.image = Image.open(image_path)
        self.position = position
        self.size = size

    def draw(self, canvas):
        canvas.paste(self.image, self.position, self.image)

    def get_bounding_box(self):
        return (self.position[0], self.position[1], self.position[0] + self.size[0], self.position[1] + self.size[1])


    def check_collision(self, ball):
        ball_bottom_center = [ball.position[0] + ball.image.width / 2, ball.position[1] + ball.image.height]
        if self.position[0] < ball_bottom_center[0] < self.position[0] + self.size[0] and \
           self.position[1] <= ball_bottom_center[1]:
            ball.velocity[1] *= -8