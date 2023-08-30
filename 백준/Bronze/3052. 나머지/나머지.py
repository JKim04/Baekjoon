#3052
a = []
for i in range(10):
    i = int(input())
    a.append(i)
b = []
for i in a:
    i %= 42
    b.append(i)
print(len(set(b)))