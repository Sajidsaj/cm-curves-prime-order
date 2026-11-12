"""Brute-force checks of the exact local laws stated in docs/NOTE.md.

Usage:  python src/check_local_laws.py [LIMIT]      (default LIMIT = 100000)
"""
import sys
from collections import Counter
from sympy import primerange
from cm_orders import orders_j0, two_squares

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 100000

# --- j = 0 (prime order with twist 3*prime): Z_l(p) = number of the six orders M such that l divides neither M nor 2(p+1) - M
z5, z7 = Counter(), Counter()
for p in primerange(11, LIMIT):
    if p % 3 != 1:
        continue
    S = orders_j0(p)
    Z5 = sum(1 for M in S if M % 5 and (2 * (p + 1) - M) % 5)
    Z7 = sum(1 for M in S if M % 7 and (2 * (p + 1) - M) % 7)
    z5[(p % 5 == 1, Z5)] += 1
    z7[(p % 7 in (1, 6), Z7)] += 1
print(f"j=0, primes p == 1 (mod 3), 11 <= p < {LIMIT}")
print("  l=5: (p == 1 mod 5, Z5):", dict(z5), " expected: (False,6) and (True,4) only")
print("  l=7: (p == +-1 mod 7, Z7):", dict(z7), " expected: (True,4) and (False,2) only")
assert set(z5) <= {(False, 6), (True, 4)} and set(z7) <= {(True, 4), (False, 2)}

# --- j = 1728 (order 2*prime with twist 2*prime): p = a^2 + b^2 (b even); numbers (p+1)/2 + b and (p+1)/2 - b
viol = Counter()
total = 0
for p in primerange(5, LIMIT):
    if p % 4 != 1:
        continue
    a, b = two_squares(p)
    if b % 2:
        a, b = b, a
    m1, m2 = (p + 1) // 2 + b, (p + 1) // 2 - b
    total += 1
    for q in (3, 7, 11, 19, 23, 31):          # inert primes q == 3 (mod 4)
        if (m1 % q == 0 or m2 % q == 0) and p % q != 1:
            viol[q] += 1
    both_prime_to_3 = (m1 % 3 != 0) and (m2 % 3 != 0)
    if both_prime_to_3 != (p % 3 == 2 or b % 3 == 0):
        viol["q=3 exact statement"] += 1
print(f"j=1728, primes p == 1 (mod 4), p < {LIMIT}: {total} primes; violations: {dict(viol) or 'none'}")
assert not viol
print("all checks passed")
