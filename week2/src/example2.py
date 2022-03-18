a = int(input("a: "))
b = int(input("b: "))

min_ = min(a, b)
max_ = max(a, b)

yak = []
for i in range(1, min_+1):
    if min_%i == 0:
        yak.append(i)
gong = []
for i in yak:
    if max_%i == 0:
        gong.append(i)
print(gong)
print(gong[-1])