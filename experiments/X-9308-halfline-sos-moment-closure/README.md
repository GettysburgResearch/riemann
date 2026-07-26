# X-9308 — Exact half-line SOS moment closure

X-9308 verifies L-9310 from the directed L-9309 basis intervals.

For degree `d=14`, every real polynomial nonnegative on `[0,infinity)` has the
form

```text
P(y) = sum a_r(y)^2 + y sum b_s(y)^2
```

with `deg a_r<=7` and `deg b_s<=6`. If `ell_k` denotes the directed residual of
the exact basis response `y^k`, the complete cone is positive exactly when

```text
H0 = (ell_(i+j))  0<=i,j<=7
H1 = (ell_(i+j+1)) 0<=i,j<=6
```

are positive semidefinite.

## Proof object

The checker reads

```text
../X-9306-real-log-portfolio-search/results/basis.json
```

as exact finite decimal rationals. It uses

```text
delta = 1/100000
```

and verifies:

1. every exact rational LDL pivot of `midpoint(H0)-delta I` is positive;
2. every exact rational LDL pivot of `midpoint(H1)-delta I` is positive;
3. the maximum row sum of the full H0 interval-radius matrix is below delta;
4. the maximum row sum of the full H1 interval-radius matrix is below delta.

No eigensolver, SDP solver, or floating-point sign enters the checker.

## PR #103 result

```text
H0 dimension                       8
H1 dimension                       7
delta                              1e-5
H0 maximum row radius              1.4140359346175754e-32
H1 maximum row radius              6.4302853244764107e-44
H0 uniform positive margin         >9.9999999999999999999999999858e-6
H1 uniform positive margin         >9.99999999999999999999999999999999999994e-6
negative or unresolved directions  0
```

Exact proof-object SHA-256:

```text
7028c2688bcd8ca783e98977bd2da6247fd70bc59f4d6f78b7df7f05a5c6096b
```

Verdict:

```text
CERTIFIED_POSITIVE_FULL_HALF_LINE_NONNEGATIVE_POLYNOMIAL_CONE
```

This closes every degree-at-most-14 response polynomial nonnegative on the
half-line at the exact 16-node PR #103 atomized-minimum table. It strictly
contains the monomial-positive cone closed by X-9307.

## Reproduction

```bash
python verify.py \
  ../X-9306-real-log-portfolio-search/results/basis.json \
  --output results/pr103-full-cone-verification.json
python -m unittest discover -s tests -v
```

## Scope

The result does not cover:

- degree above 14, which requires more horizontal nodes;
- another ordinate or count profile;
- nonpolynomial positive response families;
- matrix-valued or cross-height primitive families.

No counterexample is claimed. The exact positive closure tells the project to
move the primitive table rather than optimize further inside this cone.
