import math

from angle_unit import AngleUnit


class Vector:
    def __init__(self, coordinates) -> None:
        super().__init__()
        self.coordinates = coordinates
        self.dimension = len(coordinates)

    def plus(self, vector):
        return Vector([x + y for x, y in zip(self.coordinates, vector.coordinates)])

    def minus(self, vector):
        return Vector([round(x - y, 2) for x, y in zip(self.coordinates, vector.coordinates)])

    def times_scalar(self, scalar):
        return Vector([round(x * scalar, 3) for x in self.coordinates])

    def magnitude(self):
        powers = [c**2 for c in self.coordinates]
        return round(math.sqrt(sum(powers)), 3)

    def normalise(self):
        magnitude = self.magnitude()
        return self.times_scalar(1/magnitude)

    def dot_product(self, vector):
        return round(sum([x * y for x, y in zip(self.coordinates, vector.coordinates)]), 3)

    def angle(self, vector, angle_unit: AngleUnit):
        radians = math.acos(self.dot_product(vector) / (self.magnitude() * vector.magnitude()))
        return round(radians, 3) if angle_unit == AngleUnit.RADIANS else round(math.degrees(radians), 3)

    def __str__(self) -> str:
        return "Vector : {}".format(self.coordinates)

    def __repr__(self) -> str:
        return "Vector : {}".format(self.coordinates)

    def __eq__(self, o) -> bool:
        return self.coordinates == o.coordinates



