import sys
import unittest
import algorithms
try:
    from testfixtures import ShouldRaise
except ImportError as error:
    sys.exit("ERROR: Missing dependency: {0}".format(error))


class AlgorithmsTest(unittest.TestCase):
    def test_inverse_modulo(self):
        self.assertEqual(algorithms.extended_euclidean(67, 12), 28)

    def test_fix_negative_inverse_modulo(self):
        self.assertEqual(algorithms.extended_euclidean(19, 7), 11)

    def test_not_relatively_prime_throws_exception(self):
        with ShouldRaise(ValueError('Inputs are not relatively prime.')):
            algorithms.extended_euclidean(12, 24)
