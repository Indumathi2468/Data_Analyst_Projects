import unittest
from mean_var_std import calculate

class TestMeanVarStd(unittest.TestCase):
    def test_calculate_valid(self):
        result = calculate([0,1,2,3,4,5,6,7,8])
        self.assertIsInstance(result, dict)
        self.assertIn('mean', result)
        self.assertEqual(result['mean'][2], 4.0)
        # check one row mean and one column mean
        self.assertEqual(result['mean'][0], [3.0, 4.0, 5.0])
        self.assertEqual(result['mean'][1], [1.0, 4.0, 7.0])

    def test_calculate_value_error(self):
        with self.assertRaises(ValueError):
            calculate([1,2,3])  # less than 9 numbers

if __name__ == '__main__':
    unittest.main()
