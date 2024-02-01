def fibo(a, b):
    print(a)
    a = a + b
    print(b)
    b = a + b

    if a < 100:
        fibo(a, b)


def main():
    fibo(1, 1)


if __name__ == '__main__':
    main()




#potencia


def pot(num, exp = 2):
    base = num
    while exp > 1:
        resp = num * base
        num = resp
        exp -= 1
    return resp
print(pot(2, 4))
print(pot(3, 9))