# X-23401 — Exact fixed-ratio Mertens-shell regression

This standard-library experiment verifies the finite algebra behind
`L-23401`--`L-23403` at the distinguished ratio

\[
c=\frac23.
\]

It does **not** prove the required cofinal shell-energy estimate or RH.

## Verified identities

The checker reconstructs the Möbius function through `192` and verifies:

1. the exact divisor-dilation recurrence
   \[
   I_c(x)=-\sum_{k\ge2}I_c(x/k)
   \]
   for integer `2<=x<=96`;

2. the formal-prime-log identity
   \[
   \log x\,I_c(x)+\sum_{a\le x}\Lambda(a)I_c(x/a)
   =\sum_{cx<n\le x}\mu(n)\log(x/n);
   \]

3. the shell-binomial representation of `Delta_c^m M` through order seven;

4. finite exact Mellin rows at `s=2,3,4,5`;

5. four physical block identities
   \[
   \int_{X_0}^{X_1}{|I_c(x)|^2\over x^2}\,dx
   =\sum_{m,n}\mu(m)\mu(n)
   \left[
   {1\over\max(X_0,m,n)}
   -{1\over\min(X_1,m/c,n/c)}
   \right]_+;
   \]

6. an explicit factorization of each block matrix as
   \[
   B^T\operatorname{diag}(w)B
   \]
   with nonnegative rational segment weights;

7. the one-prime shell barrier for `c>1/2`: multiplying or dividing an
   in-shell integer by one prime exits the shell.

## Retained result

```text
divisor recurrence rows   95
prime renewal rows         95
high-order rows            672
finite Mellin rows         4
one-prime barrier rows     12,664
Gram blocks                4
verdict                    EXACT_FIXED_RATIO_MERTENS_SHELL_ALGEBRA_VERIFIED
proof-object SHA-256       0772b74939f89a2e9ac45fe38fbc0e3fd4f131c9e3d83ecdbf7ab1debb3aeff1
```

Nine mutation tests reject the half-ratio boundary, incorrect kernel scale,
wrong recurrence and renewal signs, wrong binomial orientation, wrong Mellin
numerator, a short Möbius table, and fingerprint drift.

## Run

```bash
python3 verify.py certificates/exact-c23.json \
  --output results/exact-c23-verification.json

python3 -m unittest discover -s tests -v
```

## Proof boundary

This experiment verifies exact finite identities and a positive rational Gram
factorization. It does not certify:

- a bound uniform in the block scale;
- a balanced Type-II cancellation estimate;
- square-root Mertens cancellation;
- the Riemann Hypothesis.
