N = []
for NL in range(9):
    NL = int(input())
    N.append(NL)
print(max(N))
print(N.index(max(N))+1)