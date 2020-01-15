from decimal import Decimal, getcontext


class Vector:
    def __init__(self, coordinates) -> None:
        super().__init__()
        self.coordinates = coordinates
        self.dimension = len(coordinates)
        getcontext().prec = 2

    def plus(self, vector):
        return Vector([x + y for x, y in zip(self.coordinates, vector.coordinates)])

    def minus(self, vector):
        return Vector([float(Decimal(x) - Decimal(y)) for x, y in zip(self.coordinates, vector.coordinates)])

    def times_scalar(self, scalar):
        return Vector([x * scalar for x in self.coordinates])

    def __str__(self) -> str:
        return "Vector : {}".format(self.coordinates)

    def __repr__(self) -> str:
        return "Vector : {}".format(self.coordinates)

    def __eq__(self, o) -> bool:
        return self.coordinates == o.coordinates



