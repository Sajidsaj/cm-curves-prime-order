"""Minimal affine arithmetic on y^2 = x^3 + b over GF(p) (for verification, not for production use)."""
import random
from sympy.ntheory import sqrt_mod


class Curve:
    def __init__(self, p, b):
        self.p, self.b = p, b

    def add(self, P, Q):
        p = self.p
        if P is None:
            return Q
        if Q is None:
            return P
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2:
            if (y1 + y2) % p == 0:
                return None
            lam = 3 * x1 * x1 * pow(2 * y1, -1, p) % p
        else:
            lam = (y2 - y1) * pow(x2 - x1, -1, p) % p
        x3 = (lam * lam - x1 - x2) % p
        return (x3, (lam * (x1 - x3) - y1) % p)

    def mul(self, P, k):
        R = None
        while k:
            if k & 1:
                R = self.add(R, P)
            P = self.add(P, P)
            k >>= 1
        return R

    def random_point(self):
        p = self.p
        while True:
            x = random.randrange(p)
            r = (x ** 3 + self.b) % p
            if r and pow(r, (p - 1) // 2, p) == 1:
                return (x, sqrt_mod(r, p))
