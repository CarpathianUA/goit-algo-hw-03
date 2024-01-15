import argparse
import turtle

parser = argparse.ArgumentParser(
    prog="koch_snowflake",
    description="Draws a Koch snowflake with the given recursion depth.",
)

parser.add_argument(
    "-d", "--depth", type=int, default=3, help="Recursion depth (default: %(default)s)"
)


def koch_curve(t, order, size):
    """
    Generate a Koch curve using recursion.
    
    Parameters:
        t (Turtle): The turtle object used for drawing.
        order (int): The order of the Koch curve. Determines the level of recursion.
        size (float): The length of the line segment for the current level of recursion.
    
    Returns:
        None
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=200):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    args = parser.parse_args()
    draw_koch_curve(args.depth)
