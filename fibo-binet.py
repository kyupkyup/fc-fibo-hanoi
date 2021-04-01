from math import sqrt


def fibo(x):
    return (((1 + sqrt(5))**x) - ((1 - sqrt(5))**x)) / ((2**x) * sqrt(5))


if __name__ == '__main__':
    x = 10
    print(fibo(x))
