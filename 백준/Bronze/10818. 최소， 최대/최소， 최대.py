N = int(input())
N_list = list(map(int, input().split()))

X, Y = min(N_list), max(N_list) 
print(X, Y)