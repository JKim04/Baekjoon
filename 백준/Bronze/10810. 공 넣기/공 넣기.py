N, M = map(int, input().split())

basket = []
for i in range(N):
    basket.append(0)

for i in range(M):
    i, j, k = map(int,input().split())
    for ball_in in range(i-1, j):
        basket[ball_in] = k
        
print(*basket)