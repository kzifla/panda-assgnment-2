# Assignment 1 - Phase 1
import math


class Canvas(list[str, ...]):  # our canvas class IS a list of strings
    def __init__(self, width, height):  # passing the width and height parameters
        super().__init__([" " * width for row in range(
            height)])  # we create a list, every list item (row) is made of spaces * width. The number of rows is the
        # range of height.


def print_canvas(canvas: Canvas):
    def create_row_headers(length: int):
        return "".join([str(i % 10) for i in range(length)])

    header = " " + create_row_headers(len(canvas[0]))
    print(header)
    for idx, row in enumerate(canvas):
        print(idx % 10, row, idx % 10, sep="")
    print(header)


# Usage
canvas = Canvas(100, 40)
print_canvas(canvas)
