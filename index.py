from search.search import kmp_search


string = """Lorem ipsum dodolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dodolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat. Duis aute irure dodolor in reprehenderit in
voluptate velit esse cillum dodolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

pattern = "dodolor"

kmp_search(string, pattern)
