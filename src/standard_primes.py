"""Do the primes of standard curves admit j = 0 curves of prime (or almost prime) order?"""
from sympy import isprime, primerange
from cm_orders import orders_j0

SMALL = list(primerange(2, 10 ** 4))
PRIMES = {
    "2^127-1": 2 ** 127 - 1,
    "P-192 prime": 2 ** 192 - 2 ** 64 - 1,
    "P-224 prime": 2 ** 224 - 2 ** 96 + 1,
    "2^251-9": 2 ** 251 - 9,
    "2^255-19 (Curve25519)": 2 ** 255 - 19,
    "P-256 prime": 2 ** 256 - 2 ** 224 + 2 ** 192 + 2 ** 96 - 1,
    "secp256k1 prime": 2 ** 256 - 2 ** 32 - 977,
    "2^266-3": 2 ** 266 - 3,
    "P-384 prime": 2 ** 384 - 2 ** 128 - 2 ** 96 + 2 ** 32 - 1,
    "2^414-17": 2 ** 414 - 17,
    "Ed448 prime": 2 ** 448 - 2 ** 224 - 1,
    "2^521-1": 2 ** 521 - 1,
}


def best_cofactor(p):
    best = None
    for N in orders_j0(p):
        r, h = N, 1
        for q in SMALL:
            while r % q == 0:
                r //= q
                h *= q
        if r > 1 and isprime(r) and (best is None or h < best):
            best = h
    return best


for name, p in PRIMES.items():
    assert isprime(p)
    if p % 3 != 1:
        print(f"{name:26s} p == 2 (mod 3): only supersingular j=0 curves")
        continue
    h = best_cofactor(p)
    print(f"{name:26s} smallest cofactor h of a j=0 curve (h*prime, h from primes < 10^4): {h if h else 'none'}")
