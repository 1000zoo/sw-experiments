## Resident ID

resID = input("(xxxxxx-xxxxxxx)> ")
front = (resID.split("-")[0])
back = (resID.split("-")[1])

if int(back[0]) == 1 or int(back[0]) == 3:
  print("male")
elif int(back[0]) == 2 or int(back[0]) == 4:
  print("female")
else:
  print("???")

if 0 <= int(back[1:3]) < 13:
  print("Seoul")
else:
  print("Not Seoul")

sum = 0
lit = 2
for num in front + back[:-1]:
  if lit > 9:
    lit = 2
  sum += int(num) * lit
  lit += 1

if 11 - sum % 11 == int(back[-1]):
  print("valid")
else:
  print("invalid")

