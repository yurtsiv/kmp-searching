def prepare_lps(pattern):
  lps = [0] * len(pattern)
  m = len(pattern)
  j = 0 # longest prefix in the pattern

  for i in range(1, m):
    while j > 0 and pattern[i] != pattern[j]:
      j = lps[j-1]
 
    if pattern[i] == pattern[j]:
      j += 1

    lps[i] = j

  return [0] + lps

def search_one_line(string, pattern, lps, line_num):
  positions = []

  n = len(string)
  m = len(pattern)
  lps = prepare_lps(pattern)
  j = 0  # position in pattern
  pattern = ' ' + pattern

  for i in range(0, len(string)):
    pattern_char = pattern[j+1]
    string_char = string[i]
    while j > 0 and pattern_char != string_char:
      j = lps[j]
 
    if pattern_char == string_char:
      j += 1
 
    if j == m:
      positions.append((line_num, (i - m) + 2))
      j = lps[j]

  return positions
  
def kmp_search(string, pattern):
  result = []
  lines = string.split("\n")
  lps = prepare_lps(pattern)

  for i in range(0, len(lines)):
    result.extend(
      search_one_line(lines[i], pattern, lps, i + 1)
    )

  return result
