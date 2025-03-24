from abc import ABC, abstractmethod
from curses.textpad import rectangle


class Shape(ABC):
    @abstractmethod
    def accept(self, vistor):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, vistor):
        vistor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, vistor):
        vistor.visit_rectangle(self)


class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    def visit_rectangle(self, rectangle):
        pass


class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        area = 3.14 * circle.radius**2
        print(f"Area of circle with radius {circle.radius} = {area}")

    def visit_rectangle(self, rectangle):
        area = rectangle.height * rectangle.width
        print(f"Area of rectangle with height = {rectangle.height} and width = {rectangle.width} = {area}")

class LengthCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        shape_length = 2 * 3.14 * circle.radius
        print(f"Circumference of circle with radius {circle.radius} = {shape_length}")

    def visit_rectangle(self, rectangle):
        shape_length = 2 * rectangle.height + 2 * rectangle.width
        print(f"Length of rectangle with height = {rectangle.height} and width = {rectangle.width} = {shape_length}")


circle_1 = Circle(4)
circle_2 = Circle(10)
rectangle_1 = Rectangle(2,10)
rectangle_2 = Rectangle(4,5)

shapes = [circle_1, circle_2 , rectangle_1, rectangle_2]

area_calculator = AreaCalculator()
length_calculator = LengthCalculator()

for shape in shapes:
    shape.accept(area_calculator)
    shape.accept(length_calculator)
