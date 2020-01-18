import unittest

from vector import Vector
from angle_unit import AngleUnit


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

    def test_dot_product(self):
        vector1 = Vector([-5.955, -4.904, -1.874])
        vector2 = Vector([-4.496, -8.755, 7.103])
        self.assertEqual(56.397, vector1.dot_product(vector2))

    def test_dot_product2(self):
        vector1 = Vector([7.887, 4.138])
        vector2 = Vector([-8.802, 6.776])
        self.assertEqual(-41.382, vector1.dot_product(vector2))

    def test_angle_of_two_vectors(self):
        vector1 = Vector([3.183, -7.627])
        vector2 = Vector([-2.668, 5.319])
        self.assertEqual(3.078, vector1.angle(vector2, AngleUnit.RADIANS))

    def test_angle_of_two_vectors_in_degrees(self):
        vector1 = Vector([7.35, 0.221, 5.188])
        vector2 = Vector([2.751, 8.259, 3.985])
        self.assertEqual(60.264, vector1.angle(vector2, AngleUnit.DEGREES))

    def test_is_parallel1(self):
        vector1 = Vector([-7.579, -7.88])
        vector2 = Vector([22.737, 23.64])
        self.assertEqual(True, vector1.is_parallel_to(vector2))

    def test_is_parallel2(self):
        vector1 = Vector([-2.029, 9.97, 4.172])
        vector2 = Vector([-9.231, -6.639, -7.245])
        self.assertEqual(False, vector1.is_parallel_to(vector2))

    def test_is_parallel3(self):
        vector1 = Vector([-2.328, -7.284, 1.214])
        vector2 = Vector([-1.821, 1.072, -2.94])
        self.assertEqual(False, vector1.is_parallel_to(vector2))

    def test_is_parallel4(self):
        vector1 = Vector([2.118, 4.827])
        vector2 = Vector([0, 0])
        self.assertEqual(True, vector1.is_parallel_to(vector2))

    def test_is_orthogonal1(self):
        vector1 = Vector([-7.579, -7.88])
        vector2 = Vector([22.737, 23.64])
        self.assertEqual(False, vector1.is_orthogonal_to(vector2))

    def test_is_orthogonal2(self):
        vector1 = Vector([-2.029, 9.97, 4.172])
        vector2 = Vector([-9.231, -6.639, -7.245])
        self.assertEqual(False, vector1.is_orthogonal_to(vector2))

    @unittest.skip
    def test_is_orthogonal3(self):
        vector1 = Vector([-2.328, -7.284, 1.214])
        vector2 = Vector([-1.821, 1.072, -2.94])
        self.assertEqual(True, vector1.is_orthogonal_to(vector2))

    def test_is_orthogonal4(self):
        vector1 = Vector([2.118, 4.827])
        vector2 = Vector([0, 0])
        self.assertEqual(True, vector1.is_orthogonal_to(vector2))