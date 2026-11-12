# Prime-order and twist-secure elliptic curves with complex multiplication (j = 0 and j = 1728)

Computational notes, data and verification scripts about curves `y^2 = x^3 + b` (j = 0, the family of
secp256k1) and `y^2 = x^3 + A*x` (j = 1728) over prime fields.

> **Disclaimer.** This is research / educational material. The curves listed here are **not audited and not
> standardized**. Do not use them to protect real funds or data. For production systems use well-reviewed
> curves (for example secp256k1 or Ed25519) with audited, constant-time libraries.

## What is here
| Path | Content |
|---|---|
| `docs/NOTE.md` | Short technical note: statements, proof sketches, tables |
| `src/cm_orders.py` | The possible numbers of points (6 orders for j = 0, 4 for j = 1728) via Cornacchia |
| `src/verify_curve.py` | Verify `y^2 = x^3 + b` over `2^k - c`: prime order `n` and twist `3*prime` (proof by `n*P = infinity`) |
| `src/search_special_primes.py` | Search the least `c` with a prime-order (and twist-3) j = 0 curve over `2^k - c` |
| `src/standard_primes.py` | Do standard fast primes admit prime-order j = 0 curves? |
| `src/check_local_laws.py` | Brute-force check of the exact local laws in the note |
| `src/invalid_curve_exposure.py` | Small-subgroup exposure of secp192k1, secp224k1, secp256k1 |
| `pari/verify.gp` | PARI/GP checks (independent of the Python code) |
| `data/` | tables of primes and curves |

## Quick start
```
pip install -r requirements.txt
cd src
python standard_primes.py
python verify_curve.py 256 681003 6          # p = 2^256 - 681003, b = 6
python search_special_primes.py 192 90 --twist
python check_local_laws.py 100000
python invalid_curve_exposure.py
```
PARI/GP: paste the blocks of `pari/verify.gp` (expected output is written in the comments).
Tested with Python 3.12.3 and sympy 1.14.0 (the scripts run from inside `src/`; PARI/GP is only needed for `pari/verify.gp`).


## Main results (details and caveats in `docs/NOTE.md`)
1. Over `GF(p)`, `p = 1 (mod 3)`, the six curves `y^2 = x^3 + b` have six possible orders; for `p > 7` at most two are prime,
   and the quadratic twist of a prime-order curve always has order divisible by 3 (so "prime + 3*prime" is the best possible).
2. Among standard fast primes, **only secp256k1's prime admits a prime-order j = 0 curve**: 2^255-19, P-256, P-224, 2^266-3 admit
   none with cofactor below 10^4; 2^127-1 and 2^521-1 have best cofactors 2341 and 867; P-192, P-384, Ed448, 2^251-9, 2^414-17
   are == 2 (mod 3).
3. Prime-order (and prime-order + twist `3*prime`) j = 0 curves over pseudo-Mersenne primes `2^k - c`, `k = 160 ... 521`
   (`data/special_prime_j0_table.txt`).
4. Exact local laws explaining the residue-class biases of two families of primes (j = 0: prime order with twist `3*prime`;
   j = 1728: orders `2*prime` for a curve and its twist).
5. SEC 2: `7` is the least `b` with prime order for secp256k1; `3` for secp192k1; for secp224k1 the least `b` is `2`
   (SEC 2 uses `5`, which gives an isomorphic curve).

## Related OEIS entry
A399358: primes `p` such that `y^2 = x^3 + 7` over `GF(p)` has a prime number of points.

## Author and license
Sajid Khan Hussain. Code and text under the MIT license (see `LICENSE`).
