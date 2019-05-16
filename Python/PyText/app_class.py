class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("draw")


point = Point(1, 2)
print(type(point))
print(isinstance(point, Point))
print(point.x)
