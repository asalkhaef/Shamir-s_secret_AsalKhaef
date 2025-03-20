# 🔐 Shamir's Secret Sharing in Python

This project implements **Shamir's Secret Sharing (SSS)** algorithm in Python, allowing you to securely split a secret into multiple shares and reconstruct it using a subset of those shares.

## ✨ Features
- **Secret Sharing**: Splits a secret into multiple shares using polynomial interpolation.
- **Secret Reconstruction**: Recovers the secret using Lagrange interpolation.
- **Modular Arithmetic**: Ensures security and correctness using finite field operations.

## 📜 How It Works
1. **Splitting the Secret**:
   - A secret is embedded in a polynomial of degree `threshold - 1`.
   - The polynomial is evaluated at different `x` values to generate `num_shares` unique shares.
   - Any `threshold` number of shares can reconstruct the secret.

2. **Reconstructing the Secret**:
   - Uses **Lagrange interpolation** to recover the secret from a subset of shares.
   - Works in a modular field to prevent floating-point errors.

## 🚀 Installation
This project requires **Python 3.x**. No external libraries are needed.
