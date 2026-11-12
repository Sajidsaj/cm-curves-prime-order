# Notes on prime-order and twist-secure curves with CM (j = 0, j = 1728)

Author: Sajid Khan Hussain.

## 1. Setting and known facts
Let `p = 1 (mod 3)`, `w` a primitive cube root of unity, `p = pi * conj(pi)` in `Z[w]`.
The numbers of points of `y^2 = x^3 + b` over `GF(p)` (one value for each class of `b` modulo sixth powers) are the six values
`M = Norm(pi + u)`, `u` a unit of `Z[w]`; the quadratic twist has `2(p+1) - M = Norm(pi - u)` points. Writing `p = c^2 - c*d + d^2`
these are `p + 1 - {+-(2c-d), +-(c+d), +-(c-2d)}` (Wu and Xu; Ireland and Rosen, *A Classical Introduction to Modern Number Theory*,
Chapter 18, Section 3). For `p = 1 (mod 4)`, `p = a^2 + b^2` (a odd, b even), the curves `y^2 = x^3 + A*x` have the four orders
`p + 1 +- 2a`, `p + 1 +- 2b` (Chapter 18, Section 4). If `p = 2 (mod 3)`, every `y^2 = x^3 + b` has `p + 1` points.
Both families were checked against brute-force counts (`src/cm_orders.py`).

## 2. Elementary consequences (proved)
* **R1.** For `p > 7`, at most two of the six orders are prime: if `b` is a square, `(0, sqrt b)` has order 3; if `b` is a cube, `(-cbrt b, 0)` has
  order 2. So the number of `b` in `1..p-1` giving a prime number of points is `0`, `(p-1)/6` or `(p-1)/3`.
* **R2.** `Norm(x)` for `x` in `Z[w]` is `0` or `1 (mod 3)`. Hence a prime order `N > 3` satisfies `N = 1 (mod 3)`, and the twist order
  `2(p+1) - N` is divisible by 3. The best possible twist security of a prime-order j = 0 curve is `3 * prime`.
* **R3.** For a prime `q = 2 (mod 3)` (inert in `Z[w]`): `q | Norm(pi +- u)` forces `pi = -+u^-1 (mod q)`, hence `p = 1 (mod q)`.
* **R4.** If `y^2 = x^3 + 7` has prime order over `GF(p)`, then `p = 1 (mod 3)`, 7 is a quadratic non-residue and `-7` a cubic non-residue mod `p`,
  so `p = 13, 43, 61, 67, 73 or 79 (mod 84)`.

## 3. Exact local laws
**j = 0 ("twist 3").** Let `Z_l(p)` be the number of the six orders `M` such that `l` divides neither `M` nor `2(p+1) - M`.
* `l = 7`: `Z_7(p) = 4` if `p = +-1 (mod 7)`, else `2`. *Proof:* `7 = lambda * lambdabar`, the units map isomorphically onto `F_7*`
  (`e` at `lambda`, `e^-1` at `lambdabar`); with `alpha, alpha' = pi mod lambda, lambdabar` (`alpha * alpha' = p`) the excluded `e` are
  `{+-alpha^-1, +-alpha'}`, a set of size 2 if `p = +-1 (mod 7)` and size 4 otherwise.
* `l = 5`: `Z_5(p) = 6` if `p != 1 (mod 5)`, else `4`. *Proof:* 5 is inert; the units are the norm-1 subgroup of `F_25*`; exactly 2 of 6 products
  reach `+-1` when `p = 1 (mod 5)`.
* General `l`: for a fixed unit the probability that `l` divides neither number is `1 - 2/(l+1)` (`l` inert, `p = 1 mod l`; else 1), and
  `(l-3)/(l-1)` or `(l-5)/(l-1)` (`l` split, `p = +-1 mod l` or not). These are densities (Chebotarev / Hecke equidistribution of primary
  primes); exhaustive enumeration over `(Z[w]/l)*` confirms the values.

**j = 1728.** With `p = a^2 + b^2` (b even), `M = p + 1 +- 2b = 2 * ((p+1)/2 +- b)`.
* For a prime `q = 3 (mod 4)`, `q` divides `(p+1)/2 - b` or `(p+1)/2 + b` only if `p = 1 (mod q)` (`q` is inert in `Z[i]`).
* `q = 3`: both numbers are prime to 3 iff `p = 2 (mod 3)` or `3 | b`.
* `q = 5`: if `p = +-2 (mod 5)`, 5 divides one of the two numbers (only `p = 17` survives).
* Densities: `1 - 2/(l+1)` (inert, `p = 1 mod l`; else 1) and `(l-3)/(l-1)`, `(l-5)/(l-1)` (split).

**Evidence** (ratio of frequencies of residue classes among the primes in the lists, predicted before looking at the data; primes p > 100):

| l | j = 0, twist `3*prime`: predicted / observed | j = 1728, `2*prime` and `2*prime`: predicted / observed |
|---|---|---|
| 3 | | 2.000 / 2.015 |
| 5 | 1.500 / 1.54 | classes `p = +-2` : 0 terms / 0 |
| 7 | 2.000 / 1.98 | 1.333 / 1.29 |
| 11 | 1.200 / 1.17 | 1.200 / 1.205 |
| 13 | 1.250 / 1.25 | 1.250 / 1.30 |
| 17 | 1.125 / 1.09 | 1.167 / 1.16 |
| 19 | 1.143 / 1.22 | 1.111 / 1.106 |
| 23 | 1.091 / 1.06 | 1.091 / 1.15 |

(10000 primes per family: `data/j0_prime_order_twist3_primes.txt`, `data/j1728_twist_primes.txt`.) The local statements are proved; the step from
local densities to the number of primes is the Koblitz-Zywina heuristic, which is not proved.

## 4. Computations
**Standard fast primes** (`src/standard_primes.py`): smallest cofactor `h` of a j = 0 curve of order `h * prime` (`h` made of primes below 10^4).

| Prime | Result |
|---|---|
| secp256k1 | 1 (prime order) |
| 2^127 - 1 | 2341 |
| 2^521 - 1 | 867 |
| 2^255 - 19 | 47006323 |
| P-224, P-256, 2^266 - 3 | none |
| P-192, P-384, Ed448, 2^251 - 9, 2^414 - 17 | `p = 2 (mod 3)` |

**Pseudo-Mersenne primes** `p = 2^k - c` (c odd, `p = 1 mod 3`; least `c` in this progression, tested up to about 7 * 10^5; `b` is the least `b` giving that order):

| k | prime order (c, b) | prime order and twist `3*prime` (c, b) |
|---|---|---|
| 160 | 75, 2 | 400347, 6 |
| 192 | 2625, 7 | 394323, 17 |
| 224 | 1275, 6 | 738993, 5 |
| 255 | 21109, 23 | 300769, 6 |
| 256 | 1539, 5 | 681003, 6 |
| 320 | 4875, 6 | 221517, 10 |
| 384 | 3819, 2 | not searched |
| 448 | 12303, 7 | not searched |
| 512 | 6429, 2 | not searched |
| 521 | 2305, 13 | not searched |

Every row was verified by `n * P = infinity` (this proves `#E = n` since `n` is prime). The rows `(256, 1539)`, `(256, 681003)`, `(255, 300769)`,
`(224, 738993)`, `(192, 394323)` were also checked independently with PARI (`ellcard`); the other rows were verified with the Python script only.

**SEC 2 Koblitz curves** (parameters checked against the DiSSECT database): the least `b` giving prime order is 3 for secp192k1, 7 for secp256k1 (b = 1..6 give
composite orders); for secp224k1 the least is 2, while SEC 2 uses 5 (same order; `2/5` is a sixth power, so the curves are isomorphic).

**Invalid-curve exposure** (`src/invalid_curve_exposure.py`): small subgroups (prime factors <= 10^6) of the five other curves over the same field have combined size
at least 124.1 (secp192k1), 89.2 (secp224k1), 96.4 (secp256k1) bits. This is a lower bound on what an implementation without point validation could leak; point
validation removes the attack. The quadratic twist order is divisible by 3 in all three cases (R2).

**A 256-bit random example** (`data/example_256bit_curve.txt`, checked in PARI): `p` a random 256-bit prime, `y^2 = x^3 + 13` has prime order and the twist has `3 * prime` points.

## 5. Related OEIS entry
A399358: primes `p` such that `y^2 = x^3 + 7` over `GF(p)` has a prime number of points.

## 6. Limitations
* The curves are demonstrations. CM discriminant -3 (j = 0) and -4 (j = 1728) are small by construction; random or pseudo-Mersenne primes give no "rigidity" beyond the
  stated search rule; implementations must be written and audited by experts.
* "Least c" is within the stated progression and bound. The Ireland-Rosen formula and the local densities rely on standard theorems (cubic/quadratic reciprocity, Chebotarev/Hecke);
  the finite checks were done by computer.
* Counts of primes are compared with local densities only heuristically (Koblitz-Zywina).

## References
* K. Ireland, M. Rosen, *A Classical Introduction to Modern Number Theory*, 2nd ed., GTM 84, Springer, 1990 (Chapter 18, Sections 3 and 4). ISBN 978-0-387-97329-6.
* H. Wu, G. Xu, *A Note on Koblitz Curves over Prime Fields*, IACR ePrint 2020/1136.
* D. Zywina, *A refinement of Koblitz's conjecture*, arXiv:0909.5280.
* Certicom Research, *SEC 2: Recommended Elliptic Curve Domain Parameters*, Version 2.0, 27 January 2010.
* DiSSECT, standard curves database, https://dissect.crocs.fi.muni.cz
