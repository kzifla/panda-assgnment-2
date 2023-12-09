import math

# Assignment 2 - Class Customization
# Phase 1

class Point(list[float, float]):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def __repr__(self):
        return f"[{self.x}/{self.y}]"

    def __str__(self):
        return self.__repr__()


p1 = Point(2.3, 43.14)
p2 = Point(5.53, 2.5)
p3 = Point(12.2, 28.7)

print(p1)
print([p1, p2, p3])


# At first I only used __repr__, not __str__, and it produced the same output.
# In that case, __repr__ was used to produce both methods.
# Afterwards, I added def __str__. In this case, apparently "str" prints p1,
# whereas "repr" prints [p1, p2, p3], because repr produces more detailed collections.
# However, I'm not clear on the clear distinction when if we don't use
# str at all, repr can still output both.

###################################
# Phase 2 and 3
class Shape(list[Point, ...]):
    def __init__(self, *points):
        super().__init__(points)

    def __repr__(self):
        return f"Shape {', '.join(str(point) for point in self)}"

    # for Phase 3 (tried but couldn't meet the deadline)
    # def centroid(self) -> Point :
    #     for


s1 = Shape(p1, p2, p3)
s2 = Shape(p2)
s3 = Shape()

print(s1)
print(s2)
print(s3)

###################################
# Phase 3

