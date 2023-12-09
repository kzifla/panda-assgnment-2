# Assignment 1 - Phase 4
import math


class Canvas(list[str, ...]):  # our canvas class IS a list of strings
    def __init__(self, width, height):  # passing the width and height parameters
        super().__init__([" " * width for row in range(
            height)])  # we create a list, every list item (row) is made of spaces * width. The number of rows is the
        # range of height.

    def print(self):
        def create_row_headers(length: int):
            return "".join([str(i % 10) for i in range(length)])

        header = " " + create_row_headers(len(self[0]))
        print(header)
        for idx, row in enumerate(self):
            print(idx % 10, row, idx % 10, sep="")
        print(header)

    def draw_polygon(self, *points: tuple[int, int], closed: bool = True, line_char: str = "*"):
        def draw_line_segment(start: tuple[int, int], end: tuple[int, int], line_char: str = "*"):

            def replace_at_index(s: str, r: str, idx: int) -> str:

                return s[:idx] + r + s[idx + len(r):]

            x1, y1 = start
            x2, y2 = end

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            sx = 1 if x1 < x2 else -1
            sy = 1 if y1 < y2 else -1
            error = dx - dy

            while x1 != x2 or y1 != y2:
                self[y1] = replace_at_index(self[y1], line_char, x1)

                double_error = error * 2
                if double_error > -dy:
                    error -= dy
                    x1 += sx

                if double_error < dx:
                    error += dx
                    y1 += sy

            self[y2] = replace_at_index(self[y2], line_char, x2)

        start_points = points[:-1]
        end_points = points[1:]
        if closed:
            start_points += (points[-1],)
            end_points += (points[0],)

        # Draw each segment in turn. zip is used to build tuples each consisting of a start and an end point
        for start_point, end_point in zip(start_points, end_points):
            draw_line_segment(start_point, end_point, line_char)

    def draw_line(self, start: tuple[int, int], end: tuple[int, int], line_char: str = "*"):
        self.draw_polygon(start, end, closed=False, line_char=line_char)

    def draw_rectangle(self, upper_left: tuple[int, int], lower_right: tuple[int, int],
                       line_char: str = "*"):
        x1, y1 = upper_left
        x2, y2 = lower_right

        self.draw_polygon(upper_left, (x2, y1), lower_right, (x1, y2), line_char=line_char)

    def draw_n_gon(self, center: tuple[int, int], radius: int, number_of_points: int, rotation: int = 0,
                   line_char: str = "*"):
        # Distribute the points evenly around a circle
        angles = range(rotation, 360 + rotation, 360 // number_of_points)

        points = []
        for angle in angles:
            # Convert the angle of the point to radians
            angle_in_radians = math.radians(angle)
            # Calculate the x and y positions of the point
            x = center[0] + radius * math.cos(angle_in_radians)
            y = center[1] + radius * math.sin(angle_in_radians)
            # Add the point to the list of points as a tuple
            points.append((round(x), round(y)))

        # Use the draw_polygon function to draw all the lines of the n-gon
        self.draw_polygon(*points, line_char=line_char)


# Usage
self = Canvas(100, 40)
# A simple line
self.draw_line((10, 4), (92, 19), "+")
# A polygon with five points, the last point will be connected to the first one
self.draw_polygon((7, 12), (24, 29), (42, 15), (37, 32), (15, 35))
# A rectangle from the upper-left corner to the lower-right corner
self.draw_rectangle((45, 2), (80, 27), line_char='#')
# An n-gon with a high number of points will appear like a circle
self.draw_n_gon((72, 25), 12, 20, 80, "-")

self.print()
