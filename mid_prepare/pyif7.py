exc = input("(XX dollor, yen, won)>> ")
size = int(exc.split(" ")[0])
ticker = exc.split(" ")[1]
if ticker == "dollor":
  print(size * 1200)
elif ticker == "yen":
  print(size * 10)
else:
  print(size)

