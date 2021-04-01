def fibonacci(num):
    if num <= 2:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)

if __name__ == '__main__':
    user_num = int(input('Type number : '))
    for i in range(1, user_num + 1):
        print(fibonacci(i), end=' ' )
