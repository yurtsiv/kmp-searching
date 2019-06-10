import sys
from search.search import kmp_search

def print_result(matches):
  output_str = ""
  matches_num = 0

  for line_matches in matches:
    matches_num += len(line_matches[1])
    line_res = "%11d |" % line_matches[0]
    for position in line_matches[1]:
      line_res += " %d" % position

    output_str += line_res + "\n"

  print("\nMatches found: " + str(matches_num) + "\n")
  if matches_num:
    print("Line number | Positions")
    print("-----------------------")
    print(output_str)


argv = sys.argv

help_text = """
Usasitge:

python index.py file.txt | 'string to match' 'pattern'
"""

if len(argv) != 3:
  print("Incorrect number of arguments provided\n" + help_text)
  sys.exit(0)

match_target = argv[1]
pattern = argv[2]

try:
  if '.txt' in match_target:
    result = kmp_search(open(match_target, 'r').read(), pattern)
    print_result(result)
  else:
    result = kmp_search(match_target, pattern)
    print_result(result)
except Exception as e:
  print(e)
  sys.exit(0)