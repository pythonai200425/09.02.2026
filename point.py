
class Point:
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y

    def move_left(self, value: float=0):
        self.x -= value

    def move_right(self, value: float=0):
        self.x += value

    def move_up(self, value: float=0):
        self.y -= value

    def move_down(self, value: float=0):
        self.y = value


    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

if __name__ == "__main__":
    p1 = Point(x=5.4, y=8.1)
    print(p1)

    p1.move_right(2.5)
    p1.move_up(3)

    print(p1)
