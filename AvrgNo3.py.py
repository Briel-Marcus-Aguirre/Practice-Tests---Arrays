#A3 Activity - Aguirre
score = []
for i in range (5):
  s = int(input("Score: "))
  score.append(s)

passed = 0
for s in score:
    if s >= 75:
        passed = passed + 1
print(f"{passed} out of 5 passed")
