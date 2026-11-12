"""Search p = 2^k - c (c odd, p == 1 mod 3) for the least c such that some j = 0 curve y^2 = x^3 + b has
prime order, and (with --twist) prime order AND a quadratic twist with 3*prime points.

Usage:  python src/search_special_primes.py K SECONDS [--twist]
"""
import sys
import math
import time
from sympy import isprime, primerange
from cm_orders import orders_j0

SMALL = 1
for q in primerange(5, 3000):
    SMALL *= q


def search(k, seconds, want_twist):
    start = time.time()
    c = 3 if k % 2 == 0 else 1      # c in this progression gives p == 1 (mod 3) with p odd
    first_prime_order = first_twist = None
    tested = 0
    while time.time() - start < seconds:
        p = 2 ** k - c
        if math.gcd(p, SMALL) == 1 and isprime(p):
            tested += 1
            primes = [N for N in orders_j0(p) if isprime(N)]
            if primes and first_prime_order is None:
                first_prime_order = c
            if want_twist and any((2 * (p + 1) - N) % 3 == 0 and isprime((2 * (p + 1) - N) // 3) for N in primes):
                first_twist = c
            if first_prime_order and (first_twist or not want_twist):
                break
        c += 6
    return first_prime_order, first_twist, tested, c


if __name__ == "__main__":
    k = int(sys.argv[1])
    seconds = float(sys.argv[2])
    want = "--twist" in sys.argv
    a, b, tested, last = search(k, seconds, want)
    print(f"k={k}: tested {tested} primes up to c={last}; least c with prime order: {a}; with prime order and twist 3*prime: {b}")
