with open("천지우.txt", "r", encoding="UTF8") as f1:
    d = f1.readlines()

index = d.index("천지우\n")
d.insert(index+1, "male\n")
with open("천지우.txt", "w", encoding="UTF8") as f1:
    for data in d:
        f1.write(data)