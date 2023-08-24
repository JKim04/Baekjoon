#2675
t = int(input())
for i in range(t):
    r, s = input().split()
    for j in s:
        j *= int(r)
        print(j, end='')
    print()