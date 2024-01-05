import unittest
from unittest.mock import patch
from levelsfyi-crawler import levels_fyi_crawler 

class TestLevelsFYICrawler(unittest.TestCase):

    @patch('builtins.input', side_effect=['d', 'max_tc', 'exit'])
    def test_levels_fyi_crawler_with_mock_inputs(self, mock_input):

        result = levels_fyi_crawler.main_function() 

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
