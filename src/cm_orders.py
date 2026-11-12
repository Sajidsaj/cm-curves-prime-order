"""Numbers of points of j = 0 and j = 1728 curves over GF(p), via complex multiplication.

j = 0    : y^2 = x^3 + b,  p = 1 (mod 3), p = x^2 + 3*y^2.  Six possible orders.
j = 1728 : y^2 = x^3 + A*x, p = 1 (mod 4), p = a^2 + b^2.    Four possible orders.
"""
import math
from sympy.ntheory import sqrt_mod


def _cornacchia(p, d):
    """Solve x^2 + d*y^2 = p (d = 1 or 3) for a prime p, by the Euclidean algorithm."""
    r = sqrt_mod(-d % p, p)
    if r > p // 2:
        r = p - r
    a, b = p, r
    while b * b > p:
        a, b = b, a % b
    x = b
    y = math.isqrt((p - x * x) // d)
    assert x * x + d * y * y == p
    return x, y


def two_squares(p):
    """p = a^2 + b^2 (p = 1 mod 4)."""
    return _cornacchia(p, 1)


def x2_3y2(p):
    """p = x^2 + 3*y^2 (p = 1 mod 3)."""
    return _cornacchia(p, 3)


def orders_j0(p):
    """The six possible numbers of points of y^2 = x^3 + b over GF(p), p = 1 (mod 3)."""
    x, y = x2_3y2(p)
    traces = (2 * x, -2 * x, x + 3 * y, -(x + 3 * y), x - 3 * y, -(x - 3 * y))
    return sorted({p + 1 - t for t in traces})


def orders_j1728(p):
    """The four possible numbers of points of y^2 = x^3 + A*x over GF(p), p = 1 (mod 4)."""
    a, b = two_squares(p)
    return sorted({p + 1 + s * 2 * v for v in (a, b) for s in (1, -1)})
