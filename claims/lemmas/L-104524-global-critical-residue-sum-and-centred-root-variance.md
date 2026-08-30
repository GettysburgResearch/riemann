# L-104524 — Global critical-residue sum equals centred root variance

Claim ID: `L-104524`  
Status: **PROVED EXACT**  
Created: 2026-08-22  
RH status: **not assumed**

Let `p` be a monic polynomial of degree `n>=2`, with roots

\[
z_1,\ldots,z_n
\]

counted with multiplicity. Assume that every zero `c` of `p'` is simple and is
not a zero of `p`. Define

\[
\rho_c={p(c)\over p''(c)}.
\]

Put

\[
s_j=\sum_{r=1}^n z_r^j,
\qquad
\bar z={s_1\over n}.
\]

## 1. Partial-fraction expansion

The rational function `p/p'` has residue `rho_c` at every zero `c` of `p'`.
Its polynomial part has degree one. Hence

\[
{p(z)\over p'(z)}
={z\over n}-{s_1\over n^2}
+\sum_{p'(c)=0}{\rho_c\over z-c}.
\tag{L-104524.1}
\]

On the other hand,

\[
{p'(z)\over p(z)}
=\sum_{r=1}^n{1\over z-z_r}
={n\over z}+{s_1\over z^2}+{s_2\over z^3}+O(z^{-4}).
\]

Inverting at infinity gives

\[
{p(z)\over p'(z)}
={z\over n}-{s_1\over n^2}
+{s_1^2-ns_2\over n^3}{1\over z}
+O(z^{-2}).
\]

Comparing the coefficient of `1/z` in (L-104524.1),

\[
\boxed{
\sum_{p'(c)=0}\rho_c
={s_1^2-ns_2\over n^3}
=-{1\over n^2}
  \sum_{r=1}^n(z_r-\bar z)^2.
}
\tag{L-104524.2}
\]

This sum includes every real and nonreal critical point of `p`.

## 2. Symmetric strip form

If `p` has real coefficients and its root multiset is invariant under both
conjugation and `z -> -z`, then `s_1=0` and

\[
\boxed{
-\sum_{p'(c)=0}\rho_c
={1\over n^2}\sum_{r=1}^nz_r^2.
}
\tag{L-104524.3}
\]

Writing `z_r=x_r+i y_r`, symmetry makes the imaginary parts cancel and

\[
\boxed{
-\sum_{p'(c)=0}\rho_c
={1\over n^2}
\sum_{r=1}^n(x_r^2-y_r^2).
}
\tag{L-104524.4}
\]

Thus a horizontally long zero cloud inside a fixed strip has a large negative
**total** critical-residue carrier, independently of whether the roots are all
real.

## 3. Real/nonreal critical-point split

Let

\[
\mathcal R=\{c\in\mathbb R:p'(c)=0\},
\qquad
\mathcal C=\{c\notin\mathbb R:p'(c)=0\}.
\]

Then

\[
\boxed{
-\sum_{c\in\mathcal R}\rho_c
={1\over n^2}
 \sum_{r=1}^n(z_r-\bar z)^2
+
\sum_{c\in\mathcal C}\rho_c.
}
\tag{L-104524.5}
\]

Equation (L-104524.5) identifies the exact bridge needed by the Xi residue
mean-value theorem: the main negative carrier is the centred second moment of
the complete zero set; the only correction is the sum of residues at nonreal
critical points.

## 4. Xi finite-product interface

Apply the theorem to conjugation- and parity-symmetric canonical-product
truncations of `Xi^(k-1)`.  All zeros lie in the fixed strip

\[
|\Im z|\le {1\over2}
\]

by `L-104513`.  Therefore the complete-root contribution in (L-104524.4) is
explicitly dominated by the horizontal zero ordinates, while the error is
localized to the nonreal critical points of `Xi^(k)`.

A sufficient route to the first-moment half of `RCMV104530` is consequently:

```text
1. pass (L-104524.5) through symmetric canonical-product exhaustion;
2. evaluate the centred horizontal zero second moment by the zero-counting law;
3. prove that the nonreal-critical residue sum is lower order.
```

The third step is not proved here.  The identity nevertheless turns the first
residue moment from an opaque critical-value statistic into a complete-zero
variance plus one sharply identified off-real critical correction.

## 5. Scope

Equation (L-104524.2) does not control the second residue moment and does not
by itself prove residue coherence. It supplies an exact, independently
accessible main term for `M1`; `M2` and the nonreal-critical correction remain
the analytic tasks.
