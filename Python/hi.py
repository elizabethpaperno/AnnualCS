def isVowel(c):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        return True
    if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        return True
    return False
    
def noVowels(s):
  i = 0
  counter = 0
  x = ''
  while i < len(s):
    if isVowel(s[i]):
      s = s[:i]
    else:
      s += s[i]
    i += 1
  return s

print(noVowels('aSdf'))