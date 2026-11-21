# H2 Activity - Aguirre
Title = []
Copies = []

for i in range(3):
    T = input("Title: ")
    Title.append(T)
    C = int(input("Copies: "))
    Copies.append(C)

f = input("Search Title: ")

def find(Title, f):
    for i in range(len(Title)):
        if Title[i] == f:
            return f"{f} has {Copies[i]} copies."
    return "Not in the library."

print(find(Title, f))