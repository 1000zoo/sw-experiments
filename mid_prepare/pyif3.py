time = input("(HH:MM)> ")
strtolist = time.split(":")
if strtolist[-1] == "00":
  print("O'clock")
else:
  print("not O'clock")

if time[-2:] == "00":
  print("O")
else:
  print("X")

