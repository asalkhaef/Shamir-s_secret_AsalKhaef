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


def remake_secret(threshold, total_shares, mod, shares):
    x_values = [x for x, y in shares]
    y_values = [y for x, y in shares]
    return lagrange_interpolate_at_zero(x_values, y_values, mod)
