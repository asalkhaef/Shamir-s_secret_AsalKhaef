import random


def initialize_coefficients(secret, num_shares, threshold, mod):
    secret = secret % mod  # The secret reduced modulo
    coefficients = [random.randint(1, mod) for _ in range(threshold - 1)]
    return coefficients, secret


def create_shares(secret, num_shares, threshold, mod, coefficients):
    shares = []
    # Generate each share by evaluating the polynomial at different x values
    for x in range(1, num_shares + 1):
        y = secret
        for power in range(1, threshold):
            y += coefficients[power - 1] * x ** power
        shares.append((x, y % mod))
    return shares


def display_polynomial(secret, coefficients):
    polynomial = f"f(x) = {secret}"
    for i in range(1, len(coefficients) + 1):
        polynomial += f" + {coefficients[i-1]}x^{i}"
    return polynomial


def main():
    print("****Create shares****")
    # Get user input
    secret = int(input("Enter the secret: "))
    num_shares = int(input("Enter the number of shares to create: "))
    threshold = int(input("Enter the threshold number of shares required to reconstruct the secret: "))
    mod = int(input("Enter a mod number (should be larger than the secret): "))

    # Initialize the secret sharing parameters
    coefficients, secret = initialize_coefficients(secret, num_shares, threshold, mod)

    # Display the polynomial for understanding
    polynomial = display_polynomial(secret, coefficients)
    print("\nThe polynomial used to generate shares is:")
    print(polynomial)

    # Generate and display the shares
    shares = create_shares(secret, num_shares, threshold, mod, coefficients)
    print("\nThe generated shares are:")
    for share in shares:
        print(f"Share {share[0]}: {share[1]}")


if __name__ == "__main__":
    main()
