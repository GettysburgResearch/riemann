# X-23402 — Euler-aligned dyadic-shell Selberg regression

This standard-library experiment verifies the finite formal-prime-log algebra of
`L-23405` through `n=192`.

It does **not** prove a reflected forcing estimate, a shell-energy bound, or RH.

## Verified coefficient identities

For

\[
b_2(n)=\mu(n)-\mathbf1_{2\mid n}\mu(n/2),
\qquad
a_2(n)=v_2(n)+1,
\]

and

\[
\Lambda_2^\#(n)
=\Lambda(n)+(\log2)\mathbf1_{n=2^k},
\]

the checker verifies coefficient by coefficient:

1. the local pattern
   \[
   b_2(1),b_2(2),b_2(4),b_2(8)=(1,-2,1,0);
   \]
2. the exact inverse
   \[
   a_2*b_2=\varepsilon;
   \]
3. the first logarithmic identity
   \[
   b_2\log=-\Lambda_2^\#*b_2;
   \]
4. the second logarithmic identity
   \[
   b_2\log^2
   =\Lambda_2^\#*\Lambda_2^\#*b_2
    -(\Lambda_2^\#\log)*b_2;
   \]
5. the positive Selberg coefficient identity
   \[
   b_2*(a_2\log^2)
   =\Lambda_2^\#\log
    +\Lambda_2^\#*\Lambda_2^\#.
   \]

Prime logarithms are independent formal symbols. No numerical logarithm is evaluated.

## Retained result

```text
inverse rows                    192
first logarithmic rows          192
second logarithmic rows         192
Selberg rows                    192
verdict
EXACT_EULER_ALIGNED_DYADIC_SHELL_SELBERG_ALGEBRA_VERIFIED
proof-object SHA-256
91fa01830bccf8977819f81a462cba24c4afaba2d331638ba3f5c464ac7da00c
```

Seven fail-closed tests reject a wrong local factor, either wrong weight at powers
of two, a malformed schema, insufficient coverage, and proof-object drift.

## Run

```bash
python3 verify.py certificates/exact-n192.json \
  --output results/exact-n192-verification.json

python3 -m unittest discover -s tests -v
```

## Proof boundary

The experiment certifies finite Dirichlet-convolution identities only. In
particular, coefficientwise positivity of the Selberg forcing does not by itself
bound the summatory function of its inverse at square-root scale.
