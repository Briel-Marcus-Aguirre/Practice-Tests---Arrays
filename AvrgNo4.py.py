#A4 Activity - Aguirre
Score = []
for i in range (5):
  s = input("Score: ")
  Score.append(s)

highest = Score[0]

for i in Score:
    if i > highest:
        highest = i
print("Highest:", highest)