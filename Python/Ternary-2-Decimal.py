def decimal(n):

  k = list(n)
  sum = 0
  k.reverse()
  for i in range(len(k)):
      sum = sum + (int(k[i])* (3**i))
  return sum

