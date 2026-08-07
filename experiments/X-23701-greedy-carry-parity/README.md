# X-23701 — Exact greedy carry–parity finite regression

This standard-library-only experiment replays the exact finite algebra used by
`L-23701` and `L-23703`.

## What it verifies

1. For every `2<=q<=n<25`,
   ```text
   beta_(nq)
   = #{0<=j<=n : j mod q > n mod q}/(n+1).
   ```
2. The binary Kummer digit identity for every `0<=j<=n<25`.
3. The dyadic parity convolution through `N=512`:
   ```text
   sum_(m<=N) b_2(m) 1_(floor(N/m) odd)
     = 1, -2, -2, 0, 0, ... .
   ```
4. The dyadic digit convolution through `N=512`:
   ```text
   sum_(m<=N) b_2(m) s_2(floor(N/m))
     = 1, -1, -1, -1, ... .
   ```
5. Nonnegativity and feasibility of the greedy minimum-ratio algorithm on one
   completely rational synthetic target with endpoint `X=24`.
6. Rejection of a target whose active residual becomes negative.

## Retained result

```text
carry-count checks                276
binary Kummer checks              322
digital identity limit            512
synthetic endpoint                24
synthetic minimum coefficient     0
synthetic minimum slack           0
synthetic non-diagonal blockers   0
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
bcd49b987615bad83a6468687513b6a59f8b43f396458f964f18ee7c50eddc95

tests/test_verify.py
f47b9a632fdc4012716a5bfe796529481ccdb24b214c4cb488fb68f433e5190a

results/synthetic-verification.json
7328aebc262ccafda0691c8fd7b94b6c2854d17d67f3ec2e717b5c7f650b819f

results/tests.txt
9db1bba2624cf7aed006758633914b3f3f82a6447474c9aa192851c4f623c911
```

## Proof boundary

This experiment certifies finite rational identities and mutation behavior only.
It does **not** verify:

- the true logarithmic/square-root target with directed transcendental inputs;
- the asymptotic Digital Blocker Theorem;
- the square-screw normalization;
- RH.
