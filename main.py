from turtle import *
import random

speed(1)


colorlist = ['#A70CF5', '#F5805D', '#1FF5CD', '#2754F2', '#44F227', '#AEF55D', '#F5A815', '#F43A36']
forrange = range(20,100)
turnrange = [0,90]

tracker = {
    "circle": 0,
    "triangle": 0,
    "square": 0
}


def shapeattribute():
    randcolor = random.choice(colorlist)
    lengthfor = random.choice(forrange)
    turnchoice = random.choice([left(random.choice(turnrange)), right(random.choice(turnrange))])
    penup()
    forward(lengthfor)
    str(turnchoice)
    pendown()
    color(randcolor)


def single_circle():
    shapeattribute()
    begin_fill()
    circle(50)
    end_fill()


def draw_circles():
    x = 0
    while x < 1000:
        x += 10
        if x < 1000:
            single_circle()


def square():
    shapeattribute()
    cube = 0
    begin_fill()
    while cube < 5:
        cube += 1
        if cube < 5:
            forward(50)
            left(90)
    end_fill()


def draw_squares():
    y = 0
    while y < 1000:
        y += 10
        if y < 1000:
            square()


def triangle():
    shapeattribute()
    begin_fill()
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    end_fill()


def draw_triangles():
    z = 0
    while z < 1000:
        z += 10
        if z < 1000:
            triangle()


def draw_shapes():
    shpelist = [triangle, square, single_circle]
    shapes = 0
    while shapes < 50:
        if shapes < 50:

            #Check for triangle's value
            if tracker['triangle'] <= tracker['square']:
                if tracker['triangle'] == tracker['square']:
                    if tracker['triangle'] < tracker['circle']:
                        x = random.choice([triangle, square])
                        if x in tracker.keys():
                            tracker[x] += 1
                            shapes += 1
                    else:
                        t = random.choice(shpelist)
                        if t in tracker.keys():
                            tracker[t] += 1
                            shapes += 1
                        else:
                            tracker['circle'] += 1
                            shapes += 1

                elif tracker['triangle'] < tracker['square']:
                    if tracker['triangle'] < tracker['circle']:
                        triangle()
                        tracker['triangle'] += 1
                        shapes += 1
                    else:
                        x = random.choice([triangle, single_circle])
                        if x in tracker.keys():
                            tracker[x] += 1
                            shapes += 1
                        else:
                            tracker['circle'] += 1
                            shapes += 1

            #Check for circle's value
            elif tracker['circle'] <= tracker['square']:
                if tracker['circle'] == tracker['square']:
                    if tracker['circle'] < tracker['triangle']:
                        x = random.choice([single_circle, square])
                        if x in tracker.keys():
                            tracker[x] += 1
                            shapes += 1
                        else:
                            tracker['circle'] += 1
                            shapes += 1
                    else:
                        random.choice(shpelist)
                elif tracker['circle'] < tracker['square']:
                    if tracker['circle'] < tracker['triangle']:
                        single_circle()
                        tracker['circle'] += 1
                        shapes += 1
                    else:
                        x = random.choice([triangle, single_circle])
                        if x in tracker.keys():
                            tracker[x] += 1
                            shapes += 1
                        else:
                            tracker['circle'] += 1
                            shapes += 1

            #Check for square's value
            elif tracker['square'] <= tracker['circle']:
                if tracker['square'] == tracker['circle']:
                    if tracker['square'] < tracker['triangle']:
                        x = random.choice([single_circle, square])
                        if x in tracker.keys():
                            tracker[x] += 1
                            shapes += 1
                        else:
                            tracker['circle'] += 1
                            shapes += 1
                    else:
                        random.choice(shpelist)
                elif tracker['square'] < tracker['square']:
                    if tracker['square'] < tracker['triangle']:
                        square()
                        tracker['square'] += 1
                        shapes += 1
                    else:
                        x = random.choice([triangle, square])
                        if x in tracker.keys():
                            tracker[x] += 1
                            shapes += 1

            else:
                x = random.choice(shpelist)
                if x in tracker.keys():
                    tracker[x] += 1
                    shapes += 1
                else:
                    tracker['circle'] += 1
                    shapes += 1







bgcolor("black")
draw_shapes()


done()