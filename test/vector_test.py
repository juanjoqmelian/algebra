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
        self.assertEqual(vector1.plus(vector2), Vector([3.5, 4.0, 3.2]))
