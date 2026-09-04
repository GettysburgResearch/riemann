# Arithmetic continuation of PR #792

Status: **PROPOSED analytic theorems, exact finite controls, RH inequality NOT PROVED.**
Scope: actual xi, original fixed scale v=2, all degrees; separately labelled
continuous countermodel. Independent review required.
Exact parent: `81e336a6d62d0963216ae05f809ec4df05447eb8`.
Smallest remaining gap: the signed middle prime-power range in PROOF.md (20).

Read `PROOF.md`, then `VALIDATION.md`. This addendum preserves all four
original PR #792 files byte for byte. It does not change main, a predecessor,
a canonical claim, or a formal theorem.

The proof draft supplies an exact affine-Chebyshev return to the original
observable with at most square-root-in-degree coefficient cost. In the
auxiliary coordinate the arithmetic evaluation point is s=2 and the Cayley
map is `(2-w)/(1+w)`. The coefficient is exactly

```
d_N = (-1)^N [(9/32) S_N - (3/8) E_N],
S_N = sum_(ell>=2) ell^-2 (1-3/(2ell))^(N-1),
E_N = sum_(n>=2) Lambda(n)/n^2 L_N^(-1)(3 log n)
      - (-1)^N 3*2^(N-1).
```

Every archimedean coefficient is controlled; its leading term is
`(-1)^N 3/(16N)` with an explicit `O(N^-2)` error. The pole at s=1 has
been subtracted exactly. All prime powers remain included.

The small range up to `exp(sqrt(N))` is subexponential in degree by an
absolute bound. The range above `exp(4N)` is exponentially negligible.
The signed residual between them is NOT bounded as required. Direct
termwise absolute values have exact root-limsup 2, so they cannot supply
the missing subexponential result.

A positive continuous density with error `O(x^(3/4))` gives an exact
countermodel to a PNT-only argument; its coefficient rate is `sqrt(65/41)`.
It is not the actual prime measure and does not have the zeta Euler product.

Replay from this directory, with the unmodified parent files present:

```sh
python verify_arithmetic.py --check result.json
python -O verify_arithmetic.py --check result.json
```

The checker uses only standard-library rational arithmetic. It validates
finite algebra, source normalization, the fixed parent blobs, and exact
synthetic controls. It does not prove any infinite analytic estimate or
compute the actual infinite prime sum. No external priority is claimed;
the identities are in the classical Li/Bombieri--Lagarias framework.
