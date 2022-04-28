pl = [3100, 3200, 3000, 2900]

for i, p in enumerate(pl):
  print(i, p)

for i in range(len(pl)):
  print((len(pl) - 1 - i) * 10 + 100, pl[i])
