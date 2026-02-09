

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

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return (self.x + other[0], self.y + other[1])
        elif isinstance(other, dict):
            return (self.x + other['x'], self.y + other['y'])
        else:
            return "Error..."

if __name__ == "__main__":
    p1 = Point(x=5.4, y=8.1)
    print(p1)

    p1.move_right(2.5)
    p1.move_up(3)

    print(p1)

    p2 = Point(x=2, y=2)

    print('p1 + p2', p1 + p2)

    p3 = p1 + p2
    print('p3', p3)

    print('p1 + (1.5, 0)', p1, p1 + (1.5, 0))
    print('p1 + {"x": 1.5, "y":2.1}', p1, p1 + {"x": 1.5, "y":2.1})

    print(p1 + 3)