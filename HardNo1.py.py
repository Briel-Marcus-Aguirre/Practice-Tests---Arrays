# H1 Activity - Aguirre
member = []
n = input("Name (done to stop): ")

while n != "done":
    member.append(n)
    n = input("Name (done to stop): ")

f = input("Look for: ")

def find(member, f):
    for i in range(len(member)):
        if member[i] == f:
            return f"{f} is member number {i+1}"
    return f"{f} is not a member"

print(find(member, f))