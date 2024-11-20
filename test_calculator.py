import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Test data structure with multiple test cases
        self.test_cases = [
            {
                'operation': 'add',
                'inputs': [(2, 3), (0, 0), (-1, 1)],
                'expected': [5, 0, 0]
            },
            {
                'operation': 'subtract',
                'inputs': [(5, 3), (0, 0), (-1, -1)],
                'expected': [2, 0, 0]
            },
            {
                'operation': 'multiply',
                'inputs': [(2, 3), (0, 5), (-2, 3)],
                'expected': [6, 0, -6]
            },
            {
                'operation': 'divide',
                'inputs': [(6, 2), (0, 1), (-6, 2)],
                'expected': [3, 0, -3]
            }
        ]

    def test_operations(self):
        # Map operation names to their corresponding functions
        operations = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }

        # Iterate through test cases using cursor approach
        for test_case in self.test_cases:
            operation_name = test_case['operation']
            operation_func = operations[operation_name]
            
            # Create cursor for inputs and expected results
            input_cursor = 0
            while input_cursor < len(test_case['inputs']):
                x, y = test_case['inputs'][input_cursor]
                expected = test_case['expected'][input_cursor]
                
                with self.subTest(operation=operation_name, x=x, y=y):
                    result = operation_func(x, y)
                    self.assertAlmostEqual(result, expected, 
                        msg=f"{operation_name}({x}, {y}) should be {expected}")
                
                input_cursor += 1

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main() 