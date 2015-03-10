"""
This module lets you practice WRITING AND USING FUNCTIONS that together
comprise a larger problem.

Authors: David Mutchler, Chandan Rupakheti, Claude Anderson, Katie Dion,
         their colleagues and Jesse Shellabarger.  October 2013.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

#-----------------------------------------------------------------------
# Students:  This exercise builds upon a previous exercise.
# Copy your   problem0_pascal.py  file from the previous
# session's project to the src folder of THIS session's project.
# Then you can references the   pascal_triangle   function that you
# wrote by using     problem0_pascal.pascal_triangle(...)
#-----------------------------------------------------------------------

import problem0_pascal
import zellegraphics as zg

#-----------------------------------------------------------------------
# Students:  Use the following GLOBAL CONSTANTS as needed in your code
# (but do NOT modify them).  One could implement this program without
# such global constants, but they make it easier for us to write part
# of the code and you write the rest without complicating the interface.
#-----------------------------------------------------------------------
FONT_FACE = 'courier'
FONT_SIZE = 10
CHARACTER_WIDTH = 8  # Width of one character, in pixels
CHARACTER_HEIGHT = 10  # Height of one character, in pixels
ROW_HEIGHT = 3 * CHARACTER_HEIGHT
X_MARGIN = 25
Y_MARGIN = 25


def main():
    """ Tests the   draw_pascal_triangle   function by running it. """
    #-------------------------------------------------------------------
    # STUDENTS: Add code here as desired to call TEST functions.
    #-------------------------------------------------------------------
#     test_color_shape()
#     test_draw_number()
#     test_get_shape_width()
#     test_get_shape_height()
#     test_move_shape_left_and_down()
#     test_new_shape_moved_right()

    #-------------------------------------------------------------------
    # STUDENTS: Add more tests as you see fit.
    # Judge the correctness of your code by looking at the output
    # and seeing if it is as you expect.
    #-------------------------------------------------------------------
    draw_pascal_triangle(3)
    draw_pascal_triangle(7)
    draw_pascal_triangle(15)
    draw_pascal_triangle(20)


def draw_pascal_triangle(n):
    """
    Draws rows 0 through n of Pascal's triangle, formatted nicely,
    as in the attached   draw_pascal_triangles_pictures.pdf.
    """
    # We have implemented this "top level" of the algorithm.
    # You will implement many of its sub-functions.

    # Compute the rows, and from that the zellegraphics object
    # that will be used as a holder for each number to be drawn --
    # see   draw_pascal_pictures.pdf.
    rows = problem0_pascal.pascal_triangle(n)
    shape = choose_shape(rows)

    # Construct the window in which to draw Pascal's Triangle.  Its:
    #  -- width  = number of items in the last row of the Triangle
    #                times the width of the shape that holds each item.
    #  -- height = number of rows (which is n+1)
    #                times the height of the shape that holds each item.
    title = 'Rows 0 through {} of Pascal\'s Triangle'.format(n)

    shape_width = get_shape_width(shape)
    shape_height = get_shape_height(shape)
    last_row = rows[len(rows) - 1]

    window_width = (len(last_row) * shape_width) + (2 * X_MARGIN)
    window_height = shape_height * (n + 1) + (2 * Y_MARGIN)
    window = zg.GraphWin(title, window_width, window_height)

    # Construct the shape to hold the topmost number of the Triangle.
    # It is a CLONE of   shape   but centered horizontally and
    # down Y_MARGIN from the top.  Then draw the rows of Pascal's
    # Triangle onto the given window, starting with the cloned shape.
    top_shape = shape.clone()
    top_shape.move(window.getWidth() // 2, Y_MARGIN)
    draw_pascal_rows(rows, window, top_shape)

    window.closeOnMouseClick()


def choose_shape(rows):
    """
    Returns a zellegraphics shape to be used as the template for
    holding each number in Pascal's Triangle.  The shape must be a
    circle, oval or rectangle.
    """
    # Students: You don't have to change this function, but if you wish,
    # play with the effects of:
    #  -- Change the   height_multiplier   from its default of 3.
    #  -- Change the shape to an oval or a circle or an "invisible"
    #       rectangle (one whose line width is zero), or ...
    characters_per_number = choose_characters_per_number(rows)
    height_multiplier = 3
    width = characters_per_number * CHARACTER_WIDTH
    height = height_multiplier * CHARACTER_HEIGHT

    shape = zg.Rectangle(zg.Point(-width // 2, 0),
                         zg.Point(width // 2, height))
    return shape


def choose_characters_per_number(rows):
    """
    Returns the number of characters to be used to represent each
    number in the given list-of-lists.
    """
    # Students: You can leave this as its default 6, but your pictures
    #   will look better if you return:
    #      1 + (number of digits in BIGGEST)
    #   where BIGGEST is the biggest number in the last row of the
    #   argument  rows.  (Hint: the   max  function makes this easy.)

    # Done: (if time permits).  Improve this function as described.
    return 6


def test_color_shape():
    shape = zg.Rectangle(zg.Point(100, 300), zg.Point(120, 330))
    # Test 1:
    color_shape(shape, 15)
    print('Expected, actual:', 'green', shape.getFill())
    # Test 2:
    color_shape(shape, 10)
    print('Expected, actual:', 'red', shape.getFill())


def color_shape(shape, number):
    """
    Sets the fill color of the given shape by:
      -- If the given number is odd, use 'green' as the fill color
      -- Otherwise use 'red' as the fill color
    Students: You are welcome to experiment with different colors.
    """
    # Done: 2.  Implement and test this function.

    if number % 2 != 0:
        shape.setFill('green')
    else:
        shape.setFill('red')

def test_draw_number():
    number = 1202
    shape = zg.Rectangle(zg.Point(100, 100), zg.Point(200, 200))
    window = zg.GraphWin("Test Draw Number", 400, 400)

    draw_number(number, shape, window)

def draw_number(number, shape, window):
    """
    Draws the given number as a zg.Text on the given window,
    centered inside the given shape.  Uses FONT_FACE as the face
    for the zg.Text and FONT_SIZE as the size, where FONT_FACE and
    FONT_SIZE are global constants defined at the top of this module.
    """
    # Done: 3.  Implement and test this function.

    px = ((shape.p2.x - shape.p1.x) / 2) + shape.p1.x
    py = ((shape.p2.y - shape.p1.y) / 2) + shape.p1.y
    point = zg.Point(px, py)

    text = zg.Text(point, number)
    text.setFace(FONT_FACE)
    text.setSize(FONT_SIZE)

    text.draw(window)

def test_get_shape_width():
    # Test 1:
    shape = zg.Rectangle(zg.Point(100, 300), zg.Point(120, 330))
    print('Expected, actual:', 20, get_shape_width(shape))
    # Test 2:
    shape = zg.Rectangle(zg.Point(100, 300), zg.Point(50, 260))
    print('Expected, actual:', 50, get_shape_width(shape))

def get_shape_width(shape):
    """
    Returns the width of the given shape.
    Precondition: The argument is a zellegraphics Circle, Oval,
       Rectangle or other object that has getP1 and getP2 methods.
    """
    # Done: 4.  Implement and test this function, REPLACING
    #           the "stub" below.

    width = abs(shape.p2.x - shape.p1.x)
    return width


def test_get_shape_height():
    # Test 1:
    shape = zg.Rectangle(zg.Point(100, 300), zg.Point(120, 330))
    print('Expected, actual:', 30, get_shape_height(shape))
    # Test 2:
    shape = zg.Rectangle(zg.Point(100, 300), zg.Point(50, 260))
    print('Expected, actual:', 40, get_shape_height(shape))


def get_shape_height(shape):
    """
    Returns the height of the given shape.
    Precondition: The argument is a zellegraphics Circle, Oval,
       Rectangle or other object that has getP1 and getP2 methods.
    """
    # Done: 5.  Implement and test this function, REPLACING
    #           the "stub" below.
    height = abs(shape.p2.y - shape.p1.y)
    return height

def test_move_shape_left_and_down():

    window = zg.GraphWin("Test Move Shape Left and Down", 400, 400)
    rectangle = zg.Rectangle(zg.Point(100, 100), zg.Point(200, 200))
    rectangle.draw(window)
    move_shape_left_and_down(rectangle)

    window.closeOnMouseClick()

def move_shape_left_and_down(shape):
    """
    Moves the given shape:
      -- left by HALF of its width.
      -- DOWN by its height.
    MUTATES the given shape.
    """
    # Done: 6.  Implement and test this function.

    shape.move(-1 * get_shape_width(shape) / 2, get_shape_height(shape))

def test_new_shape_moved_right():

    square = zg.Rectangle(zg.Point(100, 100), zg.Point(200, 200))
    window = zg.GraphWin("Test New Shape Moved Right", 400, 400)
    square.draw(window)

    test = zg.Rectangle(zg.Point(200, 200), zg.Point(300, 300))  # Create a square directly below where the moved square should be
    test.setFill('red')
    test.draw(window)

    new_shape_moved_right(square)
    window.closeOnMouseClick()

def new_shape_moved_right(shape):
    """
    Returns a CLONE of the given shape,
    but moved to the right the width of the given shape.
    """
    # DONE: 7.  Implement and test this function.

    clone = shape.clone()
    clone.move(get_shape_width(shape), 0)
    return clone


def draw_pascal_rows(rows, window, top_shape):
    """
    Draws the rows of Pascal's Triangle.
    """
    # Done: 8. Implement this function AS FOLLOWS:
    #   Set   shape   to be a CLONE of the given  top_shape.
    #   Loop through the given rows.  For each row:
    #     -- Draw that row by CALLING  draw_row appropriately
    #          (send   shape   as the 3rd argument)
    #     -- Move   shape   to the correct position for the NEXT row
    #          by CALLING  move_shape_left_and_down

    shape = top_shape.clone()
    for k in range(len(rows)):
        draw_row(rows[k], window, shape)
        move_shape_left_and_down(shape)

def draw_row(numbers, window, shape):
    """
    Draws the numbers in the given list of numbers on the given window.
    The numbers are drawn in a row, with each number inside a clone
    of the given shape, starting with the given shape.
    """
    # TODO: 9. Implement this function AS FOLLOWS:
    #   Set   new_shape   to be a CLONE of the given  shape.
    #   Loop through the given numbers.  For each number:
    #     -- Color  new_shape  (by CALLING the  color_shape  function)
    #     -- Draw  new_shape  on the given window
    #     -- Draw the number (by CALLING the  draw_number  function)
    #     -- Reassign  new_shape  to be a new shape constructed
    #          from  new_shape  but moving it right for the next number
    #          (by CALLING the  new_shape_moved_right  function)

    new_shape = shape.clone()
    for k in range(len(numbers)):
        color_shape(new_shape, numbers[k])
        new_shape.draw(window)
        draw_number(numbers[k], new_shape, window)
        new_shape = new_shape_moved_right(new_shape)

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
