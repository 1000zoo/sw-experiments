#string
str1 = "hello world"
str2 = "my name is jiwoo"
str3 = "nice to meet you"

string = str1 + '\n' + str2
print(str1[3:-4])
print(string.count("o"))
print(str1.index("h"))              #없으면 에러
print(str1.find("k"))               #없으면 -1
STR1 = str1.upper()
print(STR1)
new_str = str1.replace("l", "k", 3) #찾는 문자, 바꿀 문자, 바꿀 회수
print(new_str)