import ltp_cqc_a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_1(self):
        """Test swap_k with k=0 so that no items are swapped"""

        L = [1, 2, 3, 4, 5, 6]
        ltp_cqc_a1.swap_k(L, 0)
        actual = L
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)

    def test_swap_k_2(self):
        """Test swap_k with a list with an odd number of items"""

        L = [1,2,3,4,5,6,7]
        ltp_cqc_a1.swap_k(L,3)
        actual = L
        expected = [5,6,7,4,1,2,3]
        self.assertEqual(actual, expected)

    def test_swap_k_3(self):
        """Test swap_k with a list with an even number of items"""

        L = [1,2,3,4,5,6]
        ltp_cqc_a1.swap_k(L,3)
        actual = L
        expected = [4,5,6,1,2,3]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
