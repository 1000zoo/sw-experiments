class cal_reg:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third
        print(self.first, self.second, self.third)
        self.values = []

    def toColor(self, *lines):
        for line in lines:
            if line == "검":
                self.values.append(0)
            elif line == "갈":
                self.values.append(1)
            elif line == "빨":
                self.values.append(2)
            elif line == "주":
                self.values.append(3)
            elif line == "노":
                self.values.append(4)
            elif line == "초":
                self.values.append(5)
            elif line == "파":
                self.values.append(6)
            elif line == "보":
                self.values.append(7)
            elif line == "회":
                self.values.append(8)
            elif line == "하":
                self.values.append(9)
            else:
                return

    def reg_value(self):
        result = 0
        result += self.values[0]*10
        result += self.values[1]*1
        result *= 10**self.values[2]
        return result

    def reg_value_o(self):
        r = self.reg_value()
        return str(r) + "옴"

    def reg_value_k(self):
        r = self.reg_value()
        r /= 1000
        return str(r) + "k옴"

reg = cal_reg("주", "주", "빨")
reg.toColor(reg.first, reg.second, reg.third)
for p in reg.values:
    print(p, end=" ")
print()
print(reg.reg_value_o())
print(reg.reg_value_k())
