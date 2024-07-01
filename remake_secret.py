def lagrange_interpolate_at_zero(x_values, y_values, mod):
    secret = 0
    for i in range(len(y_values)):
        lagrange_basis_polynomial = 1
        for j in range(len(y_values)):
            if i == j:
                continue
            multiplicative_inverse = pow(x_values[i] - x_values[j], -1, mod)
            lagrange_basis_polynomial *= (0 - x_values[j]) * multiplicative_inverse
        lagrange_basis_polynomial *= y_values[i]
        secret = (secret + lagrange_basis_polynomial) % mod
    return secret


def remake_secret(mod, shares):
    x_values = [x for x, y in shares]
    y_values = [y for x, y in shares]
    return lagrange_interpolate_at_zero(x_values, y_values, mod)


def main():
    print("\nReconstruct the secret:")
    threshold = int(input("Enter the threshold number of shares needed to reconstruct the secret: "))
    mod = int(input("Enter the mod number used: "))
    shares_input = []
    for _ in range(threshold):
        x = int(input("Enter the x value of the share: "))
        y = int(input("Enter the y value of the share: "))
        shares_input.append((x, y))

    # Reconstruct and display the secret
    reconstructed_secret = remake_secret(mod, shares_input)
    print(f"\nThe reconstructed secret is: {reconstructed_secret}")


if __name__ == "__main__":
    main()
