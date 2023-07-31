X, Y, N = input().split()

for i in range(1, int(N)+1):
    if i % int(X) == 0 and i % int(Y) == 0:
        print('FizzBuzz')
    elif i % int(X) == 0:
        print('Fizz')
    elif i % int(Y) == 0:
        print('Buzz')
    else:
        print(i)