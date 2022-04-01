scores = [1,2,3,4,5]
scores_sum = sum(scores)
scores_avg = scores_sum / len(scores)

with open("scores.txt", "w") as f:
    f.write("총 합: ")
    f.write(str(scores_sum))
    f.write("\n평균: ")
    f.write(str(scores_avg))
