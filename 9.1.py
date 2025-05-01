def prime_factors(n, factor=2, factors=None):
    if factors is None:
        factors = []
    if n <= 1:
        return factors
    if n % factor == 0:
        factors.append(factor)
        return prime_factors(n // factor, factor, factors)
    else:
        return prime_factors(n, factor + 1, factors)
num=int(input("Enter a number:"))
prime_factors(num)
