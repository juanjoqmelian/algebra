class Vector:
    def __init__(self, coordinates) -> None:
        super().__init__()
        self.coordinates = coordinates
        self.dimension = len(coordinates)

    def plus(self, vector):
        return Vector([x + y for x, y in zip(self.coordinates, vector.coordinates)])

    def __str__(self) -> str:
        "Vector : {}".format(self.coordinates)

    def __eq__(self, o) -> bool:
        return self.coordinates == o.coordinates



