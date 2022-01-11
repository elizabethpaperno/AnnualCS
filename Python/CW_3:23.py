#ord() stands for ordinal ord ('A')-> ascii cod
ord ('A')

#chr() converts from ascii to character

# 'ABC' -> 65 66 67

#called the cesar cypher (didn't always add one)
def ShiftUppercase(c):
  if c == "Z":
    return "A"
  return chr(ord(c) + 1)

# "HI THERE" -> "IJ UIFSF"