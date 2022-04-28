num = int(input("> "))
res = num - 20
if res < 0:
  print(0)
elif res > 255:
  print(255)
else:
  print(res)

