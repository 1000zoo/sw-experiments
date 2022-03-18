a = int(input("a: "))
b = int(input("b: "))

for i in range(1,101):
    if i%a==0 and i%b == 0:
        print(i)