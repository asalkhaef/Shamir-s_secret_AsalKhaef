import random

secret = 1000
num_shares = 10
threshold = 5
mod = 68


def initialize_coefficients(secret, num_shares, threshold, mod):
    secret = secret % mod  # The secret reduced modulo prime
    coefficients = [random.randint(1, mod) for _ in range(threshold - 1)]
    return coefficients, secret


def create_shares(secret, num_shares, threshold, prime, coefficients):
    shares = []
    # Generate each share by evaluating the polynomial at different x values
    for x in range(1, num_shares + 1):
        y = secret
        for power in range(1, threshold):
            y += coefficients[power - 1] * x ** power
        shares.append((x, y % prime))
    return shares


print(initialize_coefficients(secret, num_shares, threshold, mod))
