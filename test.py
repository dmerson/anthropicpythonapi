import unittest
from main import get_pi_to_5th_decimal


class TestPiFunction(unittest.TestCase):
    """Test cases for the get_pi_to_5th_decimal function."""
    
    def test_pi_value(self):
        """Test that pi is correct to the 5th decimal place."""
        result = get_pi_to_5th_decimal()
        expected = 3.14159
        self.assertEqual(result, expected)
    
    def test_pi_type(self):
        """Test that the function returns a float."""
        result = get_pi_to_5th_decimal()
        self.assertIsInstance(result, float)
    
    def test_pi_precision(self):
        """Test that pi has at most 5 decimal places."""
        result = get_pi_to_5th_decimal()
        # Convert to string and check decimal places
        result_str = str(result)
        if '.' in result_str:
            decimal_places = len(result_str.split('.')[1])
            self.assertLessEqual(decimal_places, 5)
    
    def test_pi_range(self):
        """Test that pi is in the expected range."""
        result = get_pi_to_5th_decimal()
        self.assertGreater(result, 3.14158)
        self.assertLess(result, 3.14160)


if __name__ == '__main__':
    # Run the tests
    print(f"Testing get_pi_to_5th_decimal()...")
    print(f"Result: {get_pi_to_5th_decimal()}")
    print("\nRunning unit tests:\n")
    unittest.main()
