class Point:
    def move(self):
        print("moving")
    def draw(self):
        print("drawing")
x=Point()
x.draw()
x.move()

Point.a=20
Point.b=40
print(Point.a)
print(Point.b)