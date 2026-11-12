"""Verify that y^2 = x^3 + b over GF(2^k - c) has a prime number n of points (and optionally twist = 3*prime).

Usage:  python src/verify_curve.py K C B
Proof idea: if n is prime and n*P = infinity for a point P != infinity, then the group order is a multiple of n,
and the Hasse interval contains only one multiple of n, so #E = n exactly.
"""
import sys
import random
from sympy import isprime
from cm_orders import orders_j0
from ec import Curve


def verify(k, c, b):
    p = 2 ** k - c
    assert isprime(p) and p % 3 == 1, "p must be a prime == 1 (mod 3)"
    curve = Curve(p, b)
    pts = [curve.random_point() for _ in range(3)]
    candidates = [N for N in orders_j0(p) if all(curve.mul(P, N) is None for P in pts)]
    assert len(candidates) == 1, "could not identify the group order"
    n = candidates[0]
    twist = 2 * (p + 1) - n
    print(f"p = 2^{k} - {c}  ({p.bit_length()} bits), b = {b}")
    print(f"#E = n = {n}  ({n.bit_length()} bits), n prime: {isprime(n)}")
    print(f"twist order = {twist}; divisible by 3: {twist % 3 == 0}; twist/3 prime: {twist % 3 == 0 and isprime(twist // 3)}")
    print(f"anomalous (n == p): {n == p}")
    return n


if __name__ == "__main__":
    random.seed(1)
    k, c, b = map(int, sys.argv[1:4])
    verify(k, c, b)
