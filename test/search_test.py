import unittest
from search.search import kmp_search


class SearchTest(unittest.TestCase):
  def search_test(self):
    string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
                voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
                occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

    pattern = "do"

    self.assertEqual(
      kmp_search(string, pattern),
      [
        (1, 13), (2, 5), (2, 46), (4, 21), (4, 51), (5, 28)
      ]
    )
