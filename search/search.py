def prepare_lps(pattern):
  lps = [-1] + ([0] * (len(pattern)))

  pos = 1
  cnd = 0

  while pos < len(pattern):
    if pattern[pos] == pattern[cnd]:
      lps[pos] = lps[cnd]
    else:
      lps[pos] = cnd
      cnd = lps[cnd]

      while cnd >= 0 and pattern[pos] != pattern[cnd]:
        cnd = lps[cnd]
    
    pos += 1
    cnd += 1

  lps[pos] = cnd

  return lps

  
def kmp_search(string, pattern):
  return [()]