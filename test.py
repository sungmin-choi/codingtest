from math import sqrt



def get_divisor(n):
    divisors = set()
    for i in range(1, int(sqrt(n))+1):
        if n % i==0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

print(len(get_divisor(16)))

print()