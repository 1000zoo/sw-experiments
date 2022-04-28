def print_mxn(string, count):
  cnt = 0
  for i in range(len(string)):
    print(string[i], end="")
    cnt += 1
    if cnt >= count:
      print()
      cnt = 0
  print()
print_mxn("asdfasdfqweqwe", 3)

