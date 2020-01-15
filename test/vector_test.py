import unittest

from vector import Vector


class VectorTest(unittest.TestCase):

    def test_vector_initialisation(self):
        vector = Vector([1, 2])
        self.assertEqual(vector.coordinates, [1, 2])
        self.assertEqual(vector.dimension, 2)

    def test_add_two_vectors(self):
        vector1 = Vector([1.5, 3.2, 1.6])
        vector2 = Vector([2, 0.8, 1.6])
        self.assertEqual(Vector([3.5, 4.0, 3.2]), vector1.plus(vector2))

    def test_subtract_two_vectors(self):
        vector1 = Vector([3.2, 2.4, 5.4, 6.7])
        vector2 = Vector([3.2, 2.2, 1.4, 2.4])
        self.assertEqual(Vector([0, 0.2, 4.0, 4.3]), vector1.minus(vector2))

    def test_scalar_produce(self):
        vector = Vector([2.3, 1.1, 3.4, 9.2])
        self.assertEqual(Vector([4.6, 2.2, 6.8, 18.4]), vector.times_scalar(2))

    def test_magnitude(self):
        vector = Vector([-0.221, 7.437])
        self.assertEqual(7.44, vector.magnitude())

    def test_magnitude2(self):
        vector = Vector([8.813, -1.331, -6.247])
        self.assertEqual(10.884, vector.magnitude())

    def test_normalise_vector(self):
        vector = Vector([5.581, -2.136])
        self.assertEqual(Vector([0.934, -0.357]), vector.normalise())

    def test_normalise_vector2(self):
        vector = Vector([1.996, 3.108, -4.554])
        self.assertEqual(Vector([0.34, 0.53, -0.777]), vector.normalise())
