'''i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

'''
# Example of continue statement

j = 0
while j < 6:
  j += 1
  if j == 3:
    continue
  print(j)

  k = 1
while k < 6:
  print(k)
  k += 1
else:
  print("k is no longer less than 6")