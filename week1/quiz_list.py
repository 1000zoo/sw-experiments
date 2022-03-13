#list
a = ["kim", "lee", "cha"]
c = " ".join(a)           # list -> string
print(c)
a_str = str(a)
a_str = a_str.strip("[""]")
print(a_str)

str1 = "hello world"
str2 = "my name is jiwoo"

words = str1.split(" ")   #string -> list
words += str2.split(" ")
print(words[2:])
print(words.index('my'))        #없으면 에러
words.append("!!")
print(words)
print(words.pop())
words.reverse()
words.remove("jiwoo")
print(words)

k = [1,2,3,6,4,2,0,2,2]
k.sort()
print(k)
k.insert(3, 7)
print(k)
print(k.count(2))