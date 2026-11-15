import unittest
import calculator


class TestCalculator(unittest.TestCase):

    # ---------- Partner 1 ----------
    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)

    def test_divide(self):
        # div(a, b) returns b / a
        self.assertEqual(calculator.div(2, 10), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -1)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(9), 3)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)

    # ---------- Partner 2 ----------
    def test_add(self):
        pass

    def test_subtract(self):
        pass

    def test_divide_by_zero(self):
        pass

    def test_logarithm(self):
        pass

    def test_log_invalid_base(self):
        pass


if __name__ == "__main__":
    unittest.main()