def koi(a, b, c, d, e):
    return (a*a + b*b + c*c + d*d + e*e) % 10

def main():
    _1, _2, _3, _4, _5 = map(int, input().split())
    print(koi(_1, _2, _3, _4, _5))

if __name__ == '__main__':
    main()