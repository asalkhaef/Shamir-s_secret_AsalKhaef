import random

secret = 1000
num_shares = 10
threshold = 5
mod = 68


def initialize_coefficients(secret, num_shares, threshold, mod):
    secret = secret % mod  # The secret reduced modulo prime
    coefficients = [random.randint(1, mod) for _ in range(threshold - 1)]
    return coefficients, secret


print(initialize_coefficients(secret, num_shares, threshold, mod))
