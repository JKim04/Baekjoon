def calc(a, b):
    return (a+b)*(a-b)

def main():
    _ = input().split()
    a = int(_[0])
    b = int(_[1])
    print(calc(a, b))

if __name__ == '__main__':
    main()

