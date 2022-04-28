def print_keys(dic):
  keys = list(dic.keys())
  print(type(keys))
  for key in keys:
    print(key)

dic = {
  "이름" : "홍길동",
  "나이" : 30,
  "성별" : 0
}

print_keys(dic)
