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
