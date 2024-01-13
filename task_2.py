# Завдання 2

import turtle
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", type=int, default=3, help="Recursion level")
    parser.add_argument(
        "-c", type=int, default=3, help="Number of corners in a snowflake (minimum 3)"
    )
    return parser.parse_args()


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order: int, number_corners: int, size=150):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 150)
    t.pendown()

    if number_corners < 3:
        number_corners = 3
    for i in range(number_corners):
        koch_curve(t, order, size)
        t.right(360 / number_corners)

    window.mainloop()


def main():
    args = parse_args()
    draw_koch_snowflake(args.r, args.c)


if __name__ == "__main__":
    main()

# Examples of execution:
# - Трикутна сніжинка Коха рівня 3:
#   >> python task_2.py -r 3 -c 3
# - Чотирикутна сніжинка Коха рівня 3:
#   >> python task_2.py -r 3 -c 4
# - П'ятикутна сніжинка Коха рівня 3:
#   >> python task_2.py -r 3 -c 5
