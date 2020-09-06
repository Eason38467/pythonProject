def fibonacci(n):
    if n == 1 or n == 2:
        return 1


    # 6 + 7 # 5 + 4 + 6 + 5 #
    return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(9))