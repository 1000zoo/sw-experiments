#  list : [], tuple : ()
a = [1, 2, ["a", "b"]]
print(a[2][0])


string = "abc"
string_ = "ttt"
print(string[-1])
print(string[1:2])  #  1 이상 2 미만
print(string*3)
print(string+string_)
print(string.count("a"))
print(string_.count("t"))

#split
days = "2022-03-11"
d = days.split("-")
print(d)

#list
la = [1,2,'a','b',[1,2]]
la.append("c")
print(la)
la.reverse()
print(la)

b = [4,2,1,3,5]
b.sort()
print(b)

#dictionary
dic = {1:'kim', 2:'lee', 3:'chun'}
print(dic[3])
dic[4] = 'choi'
dic["temp"] = "temp"
print(dic)
print(dic.keys())
print(dic.values())
print('temp' in dic)
print(3 in dic)
print(5 in dic)