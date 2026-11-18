#A2 Activity - Aguirre
score = []
for i in range (5):
  s = int(input("Score: "))
  score.append(s)

total = 0
for t in score:
    total = total + t
print("Total:", total)
print("Average:", total / len(score))