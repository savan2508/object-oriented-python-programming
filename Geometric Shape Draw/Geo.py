from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Uses the rectangular class to check for the
    def falls_in_rectangle(self, rectangle):
        if rectangle.low_left.x < self.x < rectangle.upright.x and \
                rectangle.low_left.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    def distance(self, x1, y1):
        dist = ((self.x - x1) ** 2 + (self.y - y1) ** 2) ** (1 / 2)
        return dist


class Rectangle:

    def __init__(self, low_left, upright):
        self.low_left = low_left
        self.upright = upright

    def area(self):
        return (self.low_left.x - self.upright.x) * \
            (self.low_left.y - self.upright.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.low_left.x, self.low_left.y)
        canvas.pendown()
        canvas.forward(self.upright.x - self.low_left.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.low_left.y)
        canvas.left(90)
        canvas.forward(self.upright.x - self.low_left.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.low_left.y)


class GuiPoint(Point):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(5,'red')


rectangle = GuiRectangle(Point(randint(0, 100), randint(0, 100)),
                         Point(randint(100, 200), randint(100, 200)))

print('Rectangle Coordinate: ', '(',
      rectangle.low_left.x, ',',
      rectangle.low_left.y, ')', 'and',
      '(', rectangle.upright.x, ',',
      rectangle.upright.y, ')')

user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

print('Your point was inside rectangle: ', user_point.falls_in_rectangle(rectangle))
print('Your area was off by: ', rectangle.area() - user_area)

myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()
