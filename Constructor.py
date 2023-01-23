class Point():
    def __init__(self,x,y):
        self.x=x 
        self.y=y 
    def  move():
        print("moving")
    def draw():
        print("drawing")
z=Point(10,20)
print(z.x)
# print(Point(X,Y))

Point.draw()
Point.move()
# print(Point.y)

# print(z)

#The constructor is automatically being called by the compiler when intialized 
#init method's variables can be called using object of the class