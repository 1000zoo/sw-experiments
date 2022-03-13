#dictionary
dic = {
    "name" : "Jiwoo",
    "birth" : "971006",
    "stud_num" : "2017271131"
}
print(dic["name"])      #없으면 에러
key = dic.keys()
value = dic.values()
item = dic.items()
print(key)
print(value)
print(item)
print(dic.get(" "))     #없으면 None
print("Jiwoo" in dic)
print("name" in dic)
print("qwerty" in dic)
dic.clear()
print(dic)
