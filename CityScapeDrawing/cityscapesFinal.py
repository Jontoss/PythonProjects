
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: ########
#    Student name: Jonty Graver
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  CITYSCAPES
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()

#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.
# d) An extra value, either 'X' or 'O', whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6, 'O']]
fixed_plan_2 = [[2, 'B', 7, 'O']]
fixed_plan_3 = [[3, 'C', 5, 'O']]
fixed_plan_4 = [[4, 'D', 4, 'O']]
fixed_plan_5 = [[1, 'A', 9, 'X']]
fixed_plan_6 = [[2, 'B', 2, 'X']]
fixed_plan_7 = [[3, 'C', 3, 'X']]
fixed_plan_8 = [[4, 'D', 6, 'X']]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10, 'O'], [2, 'A', 5, 'O'], [3, 'A', 1, 'O']]
fixed_plan_10 = [[1, 'B', 10, 'O'], [2, 'B', 5, 'O'], [3, 'B', 1, 'O']]
fixed_plan_11 = [[1, 'C', 10, 'O'], [2, 'C', 5, 'O'], [3, 'C', 1, 'O']]
fixed_plan_12 = [[1, 'D', 10, 'O'], [2, 'D', 5, 'O'], [3, 'D', 1, 'O']]
fixed_plan_13 = [[1, 'A', 10, 'X'], [2, 'A', 5, 'X'], [3, 'A', 1, 'X']]
fixed_plan_14 = [[1, 'B', 10, 'X'], [2, 'B', 5, 'X'], [3, 'B', 1, 'X']]
fixed_plan_15 = [[1, 'C', 10, 'X'], [2, 'C', 5, 'X'], [3, 'C', 1, 'X']]
fixed_plan_16 = [[1, 'D', 10, 'X'], [2, 'D', 5, 'X'], [3, 'D', 1, 'X']]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2, 'O'],
          [2, 'B', 7, 'O'],
          [5, 'C', 6, 'O'],
          [6, 'A', 4, 'O']]
fixed_plan_18 = \
         [[1, 'D', 6, 'O'],
          [3, 'C', 5, 'O'],
          [4, 'B', 3, 'O'],
          [9, 'A', 9, 'O'],
          [10, 'D', 2, 'O']]
fixed_plan_19 = \
         [[5, 'C', 6, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'A', 5, 'O'],
          [8, 'A', 7, 'O'],
          [9, 'D', 4, 'O']]
fixed_plan_20 = \
         [[1, 'A', 4, 'O'],
          [2, 'B', 4, 'O'],
          [3, 'A', 5, 'O'],
          [4, 'D', 7, 'O'],
          [10, 'B', 10, 'O']]
fixed_plan_21 = \
         [[1, 'B', 6, 'O'],
          [3, 'A', 4, 'O'],
          [4, 'C', 4, 'O'],
          [6, 'A', 8, 'O'],
          [8, 'C', 7, 'O'],
          [9, 'B', 5, 'O'],
          [10, 'D', 3, 'O']]
fixed_plan_22 = \
         [[1, 'A', 10, 'O'],
          [2, 'A', 9, 'O'],
          [3, 'C', 10, 'O'],
          [4, 'B', 5, 'O'],
          [5, 'B', 7, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'C', 2, 'O'],
          [8, 'C', 4, 'O'],
          [9, 'A', 6, 'O'],
          [10, 'D', 7, 'O']]
fixed_plan_23 = \
         [[3, 'A', 8, 'O'],
          [4, 'C', 8, 'O'],
          [5, 'B', 4, 'O'],
          [6, 'D', 5, 'O'],
          [7, 'C', 5, 'X'],
          [8, 'A', 3, 'X'],
          [9, 'D', 2, 'X']]
fixed_plan_24 = \
         [[2, 'C', 3, 'O'],
          [3, 'B', 1, 'O'],
          [4, 'C', 3, 'X'],
          [5, 'C', 1, 'O'],
          [6, 'D', 2, 'O'],
          [7, 'B', 1, 'O'],
          [8, 'D', 2, 'O'],
          [9, 'C', 7, 'O'],
          [10, 'A', 1, 'X']]
fixed_plan_25 = \
         [[1, 'B', 7, 'X'],
          [3, 'C', 1, 'O'],
          [6, 'D', 3, 'O'],
          [7, 'A', 7, 'O'],
          [8, 'D', 3, 'X'],
          [9, 'C', 7, 'O'],
          [10, 'C', 9, 'X']]
fixed_plan_26 = \
         [[1, 'A', 6, 'O'],
          [2, 'A', 2, 'O'],
          [3, 'A', 9, 'X'],
          [4, 'D', 1, 'X'],
          [5, 'C', 7, 'O'],
          [6, 'D', 6, 'O'],
          [7, 'B', 5, 'O'],
          [8, 'A', 1, 'O'],
          [9, 'D', 10, 'X'],
          [10, 'A', 6, 'O']]

#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            if randint(1, 100) <= option_probability: # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "build_city" function.
#


# Erect buildings as per the provided city plan
def build_city(city_plan):
    # Variables with placeholder values, assigned later.
    x_position = 0
    y_position = 0
    number_floors = 0
    finished = 1

    # Def a function for the different roof to represent construction
    def construction():
        pencolor('black')
        width(3)
        setheading(180)
        forward(40)
        pendown()
        right(90)
        forward(30)
        right(90)
        forward(40)
        right(90)
        forward(30)
        penup()
        left(180)
        forward(30)
        left(90)
        forward(20)
        right(90)
        pendown()
        forward(40)
        right(90)
        forward(70)
        right(90)
        forward(20)
        right(90)
        forward(10)
        left(90)
        forward(10)
        penup()
        left(180)
        forward(10)
        right(90)
        pendown()
        forward(20)
        right(90)
        forward(10)
        penup()

########### Define the different types of buildings ##############

    def building_a():
        # Draw the first floor
        pencolor('black')
        fillcolor('light blue')
        width(1)
        goto(x_position, y_position)
        pendown()
        begin_fill()
        setheading(0)
        left(180)
        # Define floor for drawing floors and draw first floor
        def floor():
            forward(100)
            right(90)
            forward(50)
            right(90)
            forward(200)
            right(90)
            forward(50)
            end_fill()
            penup()
        floor()

        # Draw First Floor Items
        goto(x_position, y_position)
        right(90)
        forward(10)
        pendown()
        fillcolor('red2')
        begin_fill()
        right(90)
        forward(20)
        right(90)
        forward(10)
        right(90)
        forward(20)
        left(180)
        forward(20)
        right(90)
        forward(10)
        right(90)
        forward(20)
        end_fill()
        penup()
        goto(x_position, y_position + 50)
        left(90)

        # Draw additional floors
        for building in range(number_floors - 1):
            pendown()
            fillcolor('light blue')
            begin_fill()
            left(180)
            floor()
            new_y_position = ycor()
            right(180)
            forward(12.5)
            left(90)
            # Draw Windows
            for window in range(4):
              forward(20)
              pendown()
              fillcolor('red2')
              begin_fill()
              forward(25)
              right(90)
              forward(25)
              right(90)
              forward(25)
              right(90)
              forward(25)
              right(90)
              end_fill()
              penup()
              forward(25)

            goto(x_position, new_y_position + 50)
            left(180)
        # Check to see if building is under construction
        if finished == 1:
            construction()
        else:
        # Draw a Roof structure
            fillcolor('yellow')
            begin_fill()
            pendown()
            forward(100)
            left(120)
            forward(30)
            left(60)
            forward(171)
            left(60)
            forward(30)
            end_fill()
            right(180)
            penup()
            forward(30)
            right(60)
            forward(20)
            left(90)
            pendown()
            forward(20)
            pencolor('red')
            dot(13)
            penup()



    ######BUILDING A END######



    def building_b():
        # Draw the first floor
        pencolor('grey')
        fillcolor('grey')
        goto(x_position, y_position)
        setheading(0)
        # Define the floor plus windows
        def draw_floor():
            pendown()
            begin_fill()
            forward(60)
            left(90)
            forward(50)
            left(90)
            forward(120)
            left(90)
            forward(50)
            left(90)
            forward(60)
            end_fill()
            penup()
            # Windows
            forward(15)
            width(1)
            pencolor('black')
            fillcolor('alice blue')
            left(90)
            forward(25)
            pendown()
            begin_fill()
            circle(15)
            end_fill()
            left(90)
            forward(30)
            penup()
            right(180)
            forward(15)
            left(90)
            pendown()
            forward(15)
            penup()
            right(180)
            forward(15)
            pendown()
            forward(15)
            penup()
            forward(10)
            left(90)

        draw_floor() # Draw the first floor

        # Draw next set of floors if needed
        goto(x_position, y_position + 50)
        for floor in range(number_floors - 1):
            pencolor('grey')
            fillcolor('rosy brown')
            draw_floor()
            new_y_position = ycor()
            goto(x_position, new_y_position + 50)

        # Check to see if building is under construction
        if finished == 1:
            construction()
        else:
            # Draw a roof structure
            pencolor('white')
            width(3)
            forward(60)
            left(180)
            pendown()
            forward(120)
            penup()
            width(1)
            pencolor('grey')
            fillcolor('rosy brown')
            right(180)
            forward(20)
            left(90)
            pendown()
            begin_fill()
            forward(10)
            left(90)
            forward(20)
            right(90)
            forward(30)
            right(90)
            forward(120)
            right(90)
            forward(30)
            right(90)
            forward(20)
            left(90)
            forward(10)
            left(180)
            forward(10)
            left(90)
            forward(80)
            end_fill()
            penup()
            pencolor('black')
            left(180)
            forward(40)
            left(90)
            forward(10)
            write('BRICK', align='center')



########BUILDING B END#########



    def building_c():
        # Draw First floor and define floor for future use
        pencolor('dark red')
        fillcolor('dark red')
        width(1)
        goto(x_position, y_position)
        setheading(0)
        # Draw first floor
        pendown()
        begin_fill()
        forward(110)
        left(90)
        forward(50)
        left(90)
        forward(220)
        left(90)
        forward(50)
        left(90)
        forward(110)
        end_fill()
        penup()
        setheading(180)
        forward(80)
        right(90)
        # Draw doors on the first floor
        def door():
            pencolor('red')
            fillcolor('light blue')
            pendown()
            begin_fill()
            forward(30)
            right(90)
            forward(30)
            right(90)
            forward(30)
            end_fill()
            penup()
            left(90)
            forward(35)
            left(90)
        for first_floor_doors in range(3):
            door()
        left(90)
        forward(115)
        setheading(0)
        goto(x_position, y_position + 50)

        # Define and draw other floors + Windows
        def floor():
            pencolor('dark red')
            fillcolor('dark red')
            begin_fill()
            pendown()
            forward(110)
            left(90)
            forward(30)
            new_y_position = ycor()
            left(90)
            forward(220)
            left(90)
            forward(30)
            left(90)
            forward(110)
            end_fill()
            penup()
            def windows():
                fillcolor('light blue')
                left(180)
                forward(90)
                right(90)
                for floor_window in range(6):
                    pendown()
                    begin_fill()
                    forward(30)
                    right(90)
                    forward(30)
                    right(90)
                    forward(30)
                    end_fill()
                    right(180)
                    penup()
            windows()
            setheading(0)
            goto(x_position, new_y_position)
        for floors in range(number_floors - 1):
            floor()
        # Check to see if building is under construction
        if finished == 1:
            construction()
        else:
            # Draw a roof structure
            pencolor('dark red')
            fillcolor('dark red')
            pendown()
            forward(110)
            left(90)
            begin_fill()
            forward(20)
            left(90)
            forward(220)
            left(90)
            forward(20)
            end_fill()
            penup()
            left(90)
            forward(20)
            left(90)
            forward(20)
            pendown()
            begin_fill()
            forward(20)
            right(90)
            forward(180)
            right(90)
            forward(20)
            end_fill()
            penup()
            right(90)
            forward(20)
            right(90)
            forward(20)
            pendown()
            begin_fill()
            forward(20)
            left(90)
            forward(140)
            left(90)
            forward(20)
            end_fill()
            penup()



##########BUILDING C END##########



    def building_d():
        pencolor('black')
        fillcolor('grey')
        width(1)
        goto(x_position, y_position)
        setheading(0)
        # Draw First Floor and its components (windows and door)
        pendown()
        begin_fill()
        forward(100)
        left(90)
        forward(50)
        left(90)
        forward(200)
        left(90)
        forward(50)
        left(90)
        forward(100)
        end_fill()
        penup()
        # Define first floor items
        def first_floor_items():
            fillcolor('light blue')
            forward(100)
            left(90)
            forward(40)
            left(90)
            def first_floor_window():
                forward(25)
                pendown()
                begin_fill()
                circle(15)
                end_fill()
                penup()
            first_floor_window()
            # Draw the door on the first floor
            forward(75)
            left(90)
            forward(15)
            pendown()
            begin_fill()
            forward(25)
            left(180)
            forward(25)
            right(90)
            forward(20)
            right(90)
            forward(25)
            right(90)
            forward(20)
            end_fill()
            begin_fill()
            forward(20)
            right(90)
            forward(25)
            right(90)
            forward(20)
            end_fill()
            penup()
            # Move in position and draw second window
            left(180)
            forward(90)
            right(90)
            forward(25)
            left(180)
            first_floor_window()
        first_floor_items()
        setheading(0)
        goto(x_position, y_position + 50)

        # Define other floors and windows and draw them

        def floor():
            pencolor('black')
            fillcolor('grey')
            pendown()
            begin_fill()
            forward(100)
            left(90)
            forward(50)
            new_y_position = ycor()
            left(90)
            forward(200)
            left(90)
            forward(50)
            left(90)
            forward(100)
            end_fill()
            penup()
            forward(100)
            left(90)
            forward(40)
            left(90)
            def window():
                pencolor('black')
                fillcolor('light blue')
                forward(25)
                pendown()
                begin_fill()
                circle(15)
                end_fill()
                penup()
            for windows in range(4):
                window()
                forward(25)
            goto(x_position, new_y_position)
            setheading(0)

        for building in range(number_floors - 1):
            floor()

        # Check to see if building is under construction
        if finished == 1:
            construction()
        else:
            # Draw a roof structure
            # Draw the sign
            width(3)
            forward(50)
            left(135)
            pendown()
            forward(30)
            setheading(180)
            forward(60)
            left(45)
            forward(30)
            penup()
            right(180)
            forward(30)
            right(45)
            forward(30)
            pendown()
            fillcolor('light blue')
            begin_fill()
            circle(30)
            end_fill()
            penup()

            # Draw additional components


##########BUILDING D END##########



##########Randomised City Placement##########

    number_list = 0  # Used for incrementing through the lists
    for each in city_plan:
        # Check the site placements and update coordinate variables
        if city_plan[number_list][0] == 1:
            x_position = -225
            y_position = -0
        elif city_plan[number_list][0] == 2:
            x_position = 25
            y_position = 0
        elif city_plan[number_list][0] == 3:
            x_position = 275
            y_position = 0
        elif city_plan[number_list][0] == 4:
            x_position = -375
            y_position = -25
        elif city_plan[number_list][0] == 5:
            x_position = -125
            y_position = -25
        elif city_plan[number_list][0] == 6:
            x_position = 125
            y_position = -25
        elif city_plan[number_list][0] == 7:
            x_position = 375
            y_position = -25
        elif city_plan[number_list][0] == 8:
            x_position = -275
            y_position = -50
        elif city_plan[number_list][0] == 9:
            x_position = -25
            y_position = -50
        elif city_plan[number_list][0] == 10:
            x_position = 225
            y_position = -50


        # Check the number of floors and update floor variable
        if city_plan[number_list][2] == 1:
            number_floors = 1
        elif city_plan[number_list][2] == 2:
            number_floors = 2
        elif city_plan[number_list][2] == 3:
            number_floors = 3
        elif city_plan[number_list][2] == 4:
            number_floors = 4
        elif city_plan[number_list][2] == 5:
            number_floors = 5
        elif city_plan[number_list][2] == 6:
            number_floors = 6
        elif city_plan[number_list][2] == 7:
            number_floors = 7
        elif city_plan[number_list][2] == 8:
            number_floors = 8
        elif city_plan[number_list][2] == 9:
            number_floors = 9
        elif city_plan[number_list][2] == 10:
            number_floors = 10

        # Check to see if building is under construction and update variable
        if city_plan[number_list][3] == 'X':
            finished = 1
        else:
            finished = 0


        # Check building type and run building function
        if city_plan[number_list][1] == 'A':
            building_a()
        elif city_plan[number_list][1] == 'B':
            building_b()
        elif city_plan[number_list][1] == 'C':
            building_c()
        elif city_plan[number_list][1] == 'D':
            building_d()

        number_list = number_list + 1 #Update variable to cycle through list

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("Jonty Graver / Toon Town")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.
# build_city(fixed_plan_1) # <-- used for code development only, not marking
build_city(random_plan()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas(True)

#
#--------------------------------------------------------------------#
