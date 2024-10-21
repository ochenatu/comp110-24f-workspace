"""Max testing"""

__author__ = "730766896"
import unittest
from find_max import find_and_remove_max


class TestFindAndRemoveMax(unittest.TestCase):

    def test_return_value(self) -> None:
        """Make sure that find_and_remove_max returns the right max value."""
        vals: list[int] = [1, 3, 2, 5, 4]
        result = find_and_remove_max(vals)
        self.assertEqual(result, 5)

    def test_mutates_input(self) -> None:
        """Makes sure the function mutates the input as it should."""
        vals: list[int] = [1, 3, 2, 6, 4, 6]
        find_and_remove_max(vals)
        self.assertEqual(vals, [1, 3, 2, 4])

    def test_edge_case_empty_list(self) -> None:
        """Edge case - Makes sure the function returns -1 for a [] list."""
        vals: list[int] = []
        result: int = find_and_remove_max(vals)
        self.assertEqual(result, -1)


if __name__ == "__main__":
    """Main function"""
    unittest.main()
