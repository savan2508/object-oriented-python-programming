from canvas import Canvas
from shapes import Rectangle, Square

# Get the information of the canvas
canvas_width = int(input('Enter the width of the Canvas: '))
canvas_height = int(input('Enter the height of the Canvas: '))

# Get the information regarding color of the canvas
color = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input('Enter the color of the canvas(white or black): ')

# Crete a canvas with the user data:
canvas = Canvas(width=canvas_width, height=canvas_height, color=color[canvas_color])

while True:
    shape_type = input('What do you like to draw (Square or Rectangle)? Enter quit to quit. ')
    if shape_type.lower() == 'rectangle':
        rec_x = int(input('Enter the distance from the left: '))
        rec_y = int(input('Enter the distance from the top: '))
        rec_width = int(input('Enter the width of the rectangle: '))
        rec_height = int(input('Enter the height of the rectangle: '))
        red = int(input('How much red do you want in rectangle? '))
        green = int(input('How much green do you want in rectangle? '))
        blue = int(input('How much blue do you want in rectangle? '))
        rec_color = (red, green, blue)

#         Create a rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=rec_color)
        r1.draw(canvas)

    elif shape_type.lower() == 'square':
        sqr_x = int(input('Enter the distance from the left: '))
        sqr_y = int(input('Enter the distance from the top: '))
        rec_width = int(input('Enter the side of the square: '))
        red = int(input('How much red do you want in rectangle? '))
        green = int(input('How much green do you want in rectangle? '))
        blue = int(input('How much blue do you want in rectangle? '))
        sqr_color = (red, green, blue)

        # Create a square
        s1 = Square(x=sqr_x, y=sqr_y, width=rec_width, color=sqr_color)
        s1.draw(canvas)

    elif shape_type.lower() == 'quit':
        break

    else:
        print('Please provide a valid input: (square, rectangle, quit)')

canvas.make('canvas.png')
