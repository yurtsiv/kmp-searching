import unittest
from search.search import kmp_search, prepare_lps


class TestSearch(unittest.TestCase):
  def test_prepare_lps(self):
    self.assertEqual(
      prepare_lps("ababd"),
      [0, 0, 0, 1, 2, 0]
    )

  def test_search(self):
    string = """Lorem ipsum dodolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dodolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat. Duis aute irure dodolor in reprehenderit in
voluptate velit esse cillum dodolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

    pattern = "dodolor"

    self.assertEqual(
      kmp_search(string, pattern),
      [
        (1, 13), (2, 47), (4, 50), (5, 29)
      ]
    )
