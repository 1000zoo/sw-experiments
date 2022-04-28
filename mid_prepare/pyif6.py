score = int(input("> "))
if score >= 100:
  print("S")
elif score in range(80, 100):
  print("A")
elif score in range(61, 80):
  print("B")
else:
  print("C")

