apart = [[101,102],[201,202],[301,302]]

for f in apart:
  for r in f:
    print(r)

for i in range(len(apart)):
  for r in apart[len(apart)-1-i]:
    print(r)

for i in range(len(apart)):
  for j in range(len(apart[i])):
    print(apart[len(apart)-1-i][len(apart[i])-1-j])
