
def fibo(num, memo):
    if num == 1:
        memo[num] = 1
        return 1
    elif num == 2:
        memo[num] = 1
        return 1
    elif memo[num] != 0:
        return memo[num]
    else:
        return fibo(num-2, memo) + fibo(num-1, memo)


if __name__ == "__main__":
    x = 10
    memo = [0] * (x+1)
    print(fibo(x, memo))
