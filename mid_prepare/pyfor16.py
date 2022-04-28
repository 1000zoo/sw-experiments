data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

vec = []

fee = 1.00014

for d in data:
  tmp = []
  for n in d:
    tmp.append(n * fee)
  vec.append(tmp)

print(vec)
