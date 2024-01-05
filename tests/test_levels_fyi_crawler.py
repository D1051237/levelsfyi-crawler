import unittest
from unittest.mock import patch
from levelsfyi_crawler import __name__ as script_name

class TestLevelsFYICrawler(unittest.TestCase):

    @patch('builtins.input', side_effect=['d', 'max_tc', 'exit'])
    @patch(f'{script_name}.open', create=True)
    def test_script_execution(self, mock_open, mock_input):

        with self.assertRaises(SystemExit) as cm:

            with open('levelsfyi_crawler.py') as script:
                exec(script.read())

        self.assertEqual(cm.exception.code, 0)

if __name__ == '__main__':
    unittest.main()
