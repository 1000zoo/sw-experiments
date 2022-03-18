#p1

i = 1
while i <= 5:
    print("*"*i)
    i += 1

#p2
s = 0
for i in range(101):
    if i%3 == 0:
        s += i
print(s)

#p3
scores = [70,60,55,75,95,90,80,80,85,100]
avg = 0.0
for score in scores:
    avg += score
avg /= len(scores)
print(avg)