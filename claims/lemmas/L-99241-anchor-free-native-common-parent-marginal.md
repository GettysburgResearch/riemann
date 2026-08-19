# L-99241 — The SHARP-kernel factorization supplies the exact anchor-free native common-parent marginal

Claim ID: `L-99241`  
Status: **PROPOSED COMPLETE EXACT COMPOSITION THEOREM — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-19  
Depends on: `L-99240`; PR #636 `L-99210--L-99212`; compact Hall/profile and causal-row identities frozen there  
RH status: **not assumed**

## 1. Exact full-row marginal

Define the signed SHARP state

\[
 \Psi(y)
 =\sum_{n\le y}\frac{\mu(n)}{\sqrt n}T(y/n)
 =4\sqrt y\sum_{n\le y}\frac{\mu(n)}n
  -3\sum_{n\le y}\frac{\mu(n)}{\sqrt n}.
\tag{L-99241.1}
\]

For the full Möbius component row

\[
 c_X(j)=\sum_{n\le X/j}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j),
\]

substitute `L-99240.7`. Every sum and integral is finite at fixed `X`, so
finite Fubini gives the exact identity

\[
 \boxed{
 c_X(j)
 =\int_1^X\Psi(X/t)\kappa_j(t)\frac{dt}{t}.
 }
\tag{L-99241.2}
\]

Equation (L-99241.2) includes every integer activation and boundary term. It is
not an open-cell or asymptotic identity.

## 2. Alignment with compact Hall

On the strict root window `1<=x<67`, (L-99241.1) is exactly the target
coordinate Hallized in frozen `L-91690`:

\[
 \Psi(x)=\sum_{k\le x}\mu(k)T_x(k).
\]

The same Hall flow gives:

```text
positive target-exact residual source;
componentwise nonnegative current-only row bonus;
no declared score assigned to the bonus.
```

For a residual source coefficient `c>=0` at endpoint `Y`, the row coordinate is

\[
 cQ_Y(j)
 =c\int_1^YT(Y/t)\kappa_j(t)\frac{dt}{t}.
\tag{L-99241.3}
\]

Both `T` and `kappa_j` are nonnegative. Thus the residual source has a literal
positive row realization, not merely the correct target mass.

The matched Hall row bonus is retained exactly once as the nonnegative
difference proved by target-normalized row monotonicity. It is not forced
through the kernel and is never recursively copied.

## 3. Exact child restriction

If `Y_i<=Y`, then (L-99241.3) for the child is the restriction of the same
positive kernel source to `t<=Y_i`:

\[
 cQ_{Y_i}(j)
 =c\int_1^{Y_i}T(Y_i/t)\kappa_j(t)\frac{dt}{t}.
\tag{L-99241.4}
\]

Consequently same-index child placement changes only the endpoint and
provenance label. It introduces neither an affine-column interpolation nor a
boundary mode.

Cross the positive kernel source with the one random-key coordinate of
`L-99211`. The child cylinders, causal-current complement, Hall residual and
Hall bonus are then one literal source partition in the fixed row. Finite
depth follows from `Y'<=Y/67+1`.

## 4. Root marginal without a Volterra inverse

Resolve the complete labelled finite tree and integrate its nonnegative fixed
row observations. Hall and every causal edge are exact row identities, so the
aggregate equals the signed root row. Equation (L-99241.2) identifies that root
row unambiguously as `c_X(j)`.

Therefore the rank-two second-order Volterra inverse is not an antecedent of
this fixed-row construction. No smooth-cell density, derivative-jump atom, or
two-anchor coefficient is needed to determine the marginal.

## 5. Result

On the frozen compact Hall/profile and causal-row inputs,

\[
 \boxed{c_X(j)\ge0\qquad(X\ge1,\ j\ge2).}
\tag{L-99241.5}
\]

The statement is row-specific but uniform in `X`. It uses no score, ordinary
capacity, radix-four capacity, thinning, terminal reserve, or prime-square
estimate.
