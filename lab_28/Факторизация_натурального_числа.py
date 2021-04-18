def print_factorization(n: int):
    max_num = 0
    primes = {}

    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = int(n / i)
                if i > max_num:
                    max_num = i
                if i not in primes:
                    primes[i] = 0
                primes[i] += 1
                break

    for j in primes:
        if primes[j] > 1:
            print(j, '^', primes[j], sep='', end='')
        else:
            print(j, end='')
        if j < max_num:
            print('*', end='')
    print()


n = int(input())
if 1 <= n <= 10**9:
    print_factorization(n)
else:
    print('Выход за рамки диапазона')
