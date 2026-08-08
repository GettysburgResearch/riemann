# X-23701 — Exact greedy carry–parity finite regression

This standard-library-only experiment replays the exact finite algebra used by
`L-23701`, `L-23703`, and `L-23704`.

## What it verifies

1. For every `2<=q<=n<25`,
   ```text
   beta_(nq)
   = #{0<=j<=n : j mod q > n mod q}/(n+1).
   ```
2. The binary Kummer digit identity for every `0<=j<=n<25`.
3. The Möbius row collapse for every `2<=m<=n<25`:
   ```text
   sum_(k<=n/m) mu(k) beta_(n,mk)
   =(2m-n-1)/(n+1).
   ```
4. The dyadic parity convolution through `N=512`:
   ```text
   sum_(m<=N) b_2(m) 1_(floor(N/m) odd)
     = 1, -2, -2, 0, 0, ... .
   ```
5. The dyadic digit convolution through `N=512`:
   ```text
   sum_(m<=N) b_2(m) s_2(floor(N/m))
     = 1, -1, -1, -1, ... .
   ```
6. Nonnegativity and feasibility of the greedy minimum-ratio algorithm on one
   completely rational synthetic target with endpoint `X=24`.
7. Equality of the greedy vector and the independent Möbius-adjoint inverse on
   that synthetic control.
8. Rejection of a target whose active residual becomes negative.

## Retained result

```text
carry-count checks                 276
binary Kummer checks               322
Möbius row-collapse checks         276
digital identity limit             512
synthetic endpoint                 24
synthetic minimum coefficient      0
synthetic minimum slack            0
synthetic adjoint mismatches        0
synthetic convexity failures       0
synthetic non-diagonal blockers    0
verdict
SYNTHETIC_GREEDY_CARRY_PARITY_ALGEBRA_VERIFIED
```

The synthetic target is

```text
w(q)=(X-q)/(qX).
```

It is chosen only because it is rational and has the same nonnegative
upper-triangular endpoint geometry as the logarithmic prime-ramp target. The
result does not claim that its blocker pattern matches the true target.

## Commands

```bash
python verify.py
python -m unittest discover -s tests -v
```

## SHA-256 ledger

```text
verify.py
def79f7b5d1906e0cd0dc8e18ace7ddaf80c0f746b1ce0db92e7156e908731a4

tests/test_verify.py
8584f1b25b8136190493d89d5cc0dc6f1d221ba6fe5fae8e3fccacf6878b9043

results/synthetic-verification.json
82548da5e72c68044a80e15a46b20750c5cf53b3322873794c439164d4237bbc

results/tests.txt
49f3d021e5ff936732742cd3f69ca38fa39c617d96cde5e730ef372fe69027cc
```

## Proof boundary

This experiment certifies finite rational identities and mutation behavior only.
It does **not** verify:

- the true logarithmic/square-root target with directed transcendental inputs;
- discrete convexity for the prime-ramp adjoint;
- the asymptotic Digital Blocker Theorem;
- the square-screw normalization;
- RH.
