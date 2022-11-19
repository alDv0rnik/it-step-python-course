def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x


print(unique_list([1, 15, 35, 4, 1, 15])) 