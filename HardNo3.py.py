# H3 Activity - Aguirre
Votes = []

V = input("Vote (done to stop): ")

while V != "done":
    Votes.append(V)
    V = input("Vote (done to stop): ")
    
n = input("Candidate: ")

no_votes = []
def count(items, n):
    for i in range(len(Votes)):
        if Votes[i] == n:
            no_votes.append(i)
    return (f"{n} got {len(no_votes)} vote(s)")
            
print(count(Votes, n))