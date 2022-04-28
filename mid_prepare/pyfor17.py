ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

lowindex = ohlc[0].index("low")

for d in ohlc:
  print(d[lowindex])

for i in range(1, len(ohlc)):
  if ohlc[i][lowindex] > 150:
    print(ohlc[i][lowindex])

openindex = ohlc[0].index("open")
closeindex = ohlc[0].index("close")

for i in range(1, len(ohlc)):
  if ohlc[i][openindex] <= ohlc[i][closeindex]:
    print(ohlc[i][closeindex])
