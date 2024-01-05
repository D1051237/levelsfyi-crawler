import unittest
from unittest.mock import patch
from levelsfyi_crawler import main_function

class TestLevelsFYICrawler(unittest.TestCase):

    @patch('builtins.input', side_effect=['d', 'max_tc', 'exit'])
    def test_main_function(self, mock_input):

        result = main_function()

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
