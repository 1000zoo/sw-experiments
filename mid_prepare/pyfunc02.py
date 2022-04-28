def print_max(*input):
  max = -999
  for i in input:
    if i > max:
      max = i
  print(i)

print_max(1,2,3,4,5)
