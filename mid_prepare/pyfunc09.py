def pickup_even(mlist):
  rlist = []
  for l in mlist:
    if l % 2 == 0:
      rlist.append(l)
  return rlist
print(pickup_even([1,2,3,4,5,6,7,8,9]))

