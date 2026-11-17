#E4 Activity - Aguirre
names = []
n = input("Name (done to stop): ")
while n != "done":
    names.append(n)
    n = input("Name (done to stop): ")
print(names)
print(f"{len(names)} names stored")
