#8958
n = int(input())

for i in range(n):
    ox = list(input())
    score = 0
    total_score = 0
    for j in ox:
        if j == 'O':
            score += 1
        else:
            score = 0
        total_score += score
    print(total_score)