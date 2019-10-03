result_f = open("result.txt")
scores = dict()
for l in result_f:
    name, score =l.split()
    scores[score]=name
result_f.close()

for score in sorted(scores.keys(), reverse=True):
    print(scores[score], " ", score)
