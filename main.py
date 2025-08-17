import turtle


def cunt(t, x, y, length, level, max_level):
    if level > max_level:
        return

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(length)

    new_y = y - 60
    new_length = length / 3

    cunt(t, x, new_y, new_length, level + 1, max_level)
    cunt(t, x + 2 * new_length, new_y, new_length, level + 1, max_level)


def main():
    t = turtle.Turtle()
    t.speed("fastest")
    t.pensize(3)

    screen = turtle.Screen()
    screen.setup(800, 600)

    start_x = -300
    start_y = 200
    initial_length = 600
    levels = 5

    cunt(t, start_x, start_y, initial_length, 0, levels)

    t.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()