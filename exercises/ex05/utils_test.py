"""Utils testing"""

__author__ = "730766896"
import unittest
from utils import only_evens, sub, add_at_index


class TestUtils(unittest.TestCase):

    def test_only_evens(self) -> None:
        """Make sure that find_and_remove_max returns the right max value."""
        vals: list[int] = [1, 3, 2, 5, 4]
        result = only_evens(vals)
        self.assertEqual(result, [2, 4])

    def test_sub(self) -> None:
        """Makes sure the function mutates the input as it should."""
        vals: list[int] = [1, 3, 2, 5, 4]
        result = sub(vals, 2, 3)
        self.assertEqual(result, [2, 5])

    def test_edge_case_add_at_index(self) -> None:
        """Edge case - Makes sure the function does IndexError properly"""
        try:
            add_at_index([1, 3, 2], 4, -1)
        except IndexError as x:
            assert str(x) == "Index is out of bounds for the input list"
        else:
            assert False, "Failed: Negative index needs to raise IndexError"


if __name__ == "__main__":
    """Main function"""
    unittest.main()
