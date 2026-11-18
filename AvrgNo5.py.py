#A5 Activity - Aguirre
Names = []
for i in range (5):
  n = input("Name: ")
  Names.append(n)

who = input("Look For: ")

count = 0

for n in Names:
  if n == who:
    count = count + 1

if count > 0:
    print(f"{who} is in the list")
else:
    print(f"{who} is not in the list")