ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

oind = ohlc[0].index("open")
hind = ohlc[0].index("high")
lind = ohlc[0].index("low")
cind = ohlc[0].index("close")

vol = []

for i in range(1, len(ohlc)):
  vol.append(abs(ohlc[i][hind] - ohlc[i][lind]))

print(vol)


