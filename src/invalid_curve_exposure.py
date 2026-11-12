"""Small-subgroup ("invalid curve") exposure of the SEC 2 Koblitz curves of j-invariant 0.

For p = 1 (mod 3) the curves y^2 = x^3 + b' over GF(p) have six possible orders; one of them is the order n of the
standard curve. The other five curves contain subgroups of small prime-power order. An implementation that multiplies
an unvalidated, attacker-chosen point by a static secret can leak the secret modulo each such small order.
This script reports log2 of the product of the distinct small prime powers (factors <= 10^6) over the five other
curves: a LOWER bound on what such an attack could reveal. Point validation removes the attack.
"""
import math
from sympy import primerange
from cm_orders import orders_j0

PARAMS = {  # prime p, group order n of the standard curve (SEC 2 / DiSSECT)
    "secp192k1": (2 ** 192 - 2 ** 32 - 4553, 6277101735386680763835789423061264271957123915200845512077),
    "secp224k1": (2 ** 224 - 2 ** 32 - 6803, 26959946667150639794667015087019640346510327083120074548994958668279),
    "secp256k1": (2 ** 256 - 2 ** 32 - 977, 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141),
}
SMALL = list(primerange(2, 10 ** 6))

for name, (p, n) in PARAMS.items():
    orders = orders_j0(p)
    assert n in orders
    best = {}
    for M in orders:
        if M == n:
            continue
        r = M
        for q in SMALL:
            if r % q == 0:
                e = 0
                while r % q == 0:
                    r //= q
                    e += 1
                best[q] = max(best.get(q, 0), e)
            if q * q > r and r < 10 ** 12:
                break
    bits = sum(e * math.log2(q) for q, e in best.items())
    twist = 2 * (p + 1) - n
    r, h = twist, 1
    for q in SMALL:
        while r % q == 0:
            r //= q
            h *= q
    print(f"{name}: small subgroups over the 5 other curves >= {bits:.1f} bits; "
          f"twist order = {h} * (rest of {r.bit_length()} bits), twist divisible by 3: {twist % 3 == 0}")
