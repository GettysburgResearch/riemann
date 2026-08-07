# R-26201 — The conditional-Hankel carry closure fails

Claim ID: `R-26201`  
Title: The zero-mass qualifier does not repair the false Hankel kernel in the frozen carry proposal  
Status: **REFUTATION / SCOPE CORRECTION**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Frozen source: PR #243 at `225c5e3d231ac23b6f487cd43e0dc89d48d3db1c`  
Review sources: PRs #255 and #257

## 1. Frozen claim being withdrawn

The frozen `L-23603` attempted to represent the interior contribution of the
dyadically aligned carry Green profile by a positive conditional-Hankel square.
Its first-cell generator was

\[
 f(t)=8e^t-7e^{t/2}-\frac32t e^{t/2}.
\]

The proposed argument asserted that restricting to zero-mass test measures was
enough to make the associated Hankel form positive.

## 2. Exact obstruction

Conditional positivity on every zero-mass measure forces positive
semidefiniteness of the mixed derivative kernel. At the first boundary point,
the required two-by-two determinant is

\[
\begin{aligned}
 f''(0)f''''(0)-f'''(0)^2
 &=\frac{19}{4}\frac{109}{16}-36\\
 &=-\frac{233}{64}<0.
\end{aligned}
\]

Thus the derivative Hankel kernel is indefinite. The zero-mass restriction does
not remove this obstruction.

Consequently the middle line of frozen equation `L-23603.15`, and every later
sign conclusion depending on it, is false at the stated scope.

## 3. What remains valid

This refutation does **not** invalidate:

1. the exact carry interpretation and affine Möbius contraction of `L-23601`;
2. the closed finite triangular inverse;
3. the continuum profile
   \[
   \mathfrak C(y)=\sum_{d\le y}\frac{\mu(d)}{\sqrt d}
   \left(8\sqrt{y/d}-7-\frac32\log(y/d)\right);
   \]
4. its Mellin transform with the reciprocal-zeta factor;
5. the dyadic alignment `b_2`, its positive inverse coefficients, generalized
   von Mangoldt weights, and digital endpoint identities;
6. the conditional deduction `\mathfrak C\ge0 => RH`.

Pointwise positivity of `\mathfrak C` is **unproved**, not refuted.

## 4. Replacement discipline

A replacement is not permitted to:

- reuse the same conditional-Hankel kernel under a new name;
- infer positivity merely from alternating derivatives of a one-variable
  profile;
- turn the reflected modulus square into an analytic square;
- delete the coherent fixed-ratio Möbius mode;
- infer a cofinal estimate from a finite positive ladder.

The continuation on this branch instead constructs a positive compact
**boundary exponential B-spline**, derives an exact parity-renewal identity, and
places the unresolved arithmetic only in a source-specific reflected remainder
estimate. No Hankel positivity of `f(x+y)` is asserted.

## 5. Status boundary

The frozen proof candidate on PR #243 is not a proof of RH. The exact carry and
digital algebra are retained as dependencies; the conditional-Hankel closure is
withdrawn and is not used by the new proposal.
