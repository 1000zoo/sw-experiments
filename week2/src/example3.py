a = int(input("a: "))

binary = []
while a > 1:
    binary.append(a%2)
    a = int(a / 2)
binary.append(a)
binary.reverse()
print(binary)
result = ""
for b in binary:
    result += str(b)

result += " (2)"
print(result)