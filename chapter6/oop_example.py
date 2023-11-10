class Point:
    color = "blue"
    def __init__(self, a, b):  # args constructor
        self.a = a
        self.b = b

    def draw(self):  # method creaction
        print(f"drawing from point {self.a} to point {self.b}")
        print(Point.color)


point1 = Point(1, 2)  # class instance
point1 = Point(5, 8)  # class instance
point1.draw()
