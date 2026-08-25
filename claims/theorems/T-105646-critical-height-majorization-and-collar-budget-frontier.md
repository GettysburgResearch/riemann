# T-105646 — Critical-height majorization supplies an unconditional collar Lyapunov function

Claim ID: `T-105646`  
Status: **MAJOR EXACT FINITE-PACKET ADVANCE; COFINAL XI ENDPOINT TRANSFER OPEN**  
Created: 2026-08-25  
Depends on: `T-105640--T-105645`; `L-105646`  
RH status: **unproved**

## 1. Differentiation decreases every convex upper-height moment

For a polynomial `p` and every horizontal line `H`,

\[
\boxed{
\sum_{p'(c)=0}
(\operatorname{Im}c-H)_+^q
\le
\sum_{p(\rho)=0}
(\operatorname{Im}\rho-H)_+^q
\qquad(q\ge1).
}
\tag{T-105646.1}
\]

More generally, the same inequality holds for every nonnegative convex
nondecreasing function of the imaginary part.

The proof is exact linear algebra:

```text
roots of p' = eigenvalues of the root-diagonal compression;
imaginary parts of those eigenvalues are Schur-majorized by Im(compression);
compression eigenvalues interlace the parent root heights.
```

Thus (T-105646.1) is a distributional strengthening of horizontal
Gauss--Lucas.  It is not merely a bound on the highest zero.

## 2. The first penetration moment is a derivative-ladder Lyapunov function

Define

\[
\mathfrak H_H(p)
=\sum_{p(\rho)=0}(\operatorname{Im}\rho-H)_+.
\]

Then

\[
\boxed{
\mathfrak H_H(p')\le\mathfrak H_H(p).
}
\tag{T-105646.2}
\]

Iterating down a finite derivative ladder gives

\[
\boxed{
\mathfrak H_H(p^{(r)})
\le\mathfrak H_H(p)
\qquad(r\ge0).
}
\tag{T-105646.3}
\]

This is the missing aggregate counterpart to the pointwise height inequality
`beta_(r+1)<=beta_r`.

## 3. Parent depth pays aggregate derivative source charge

At the base Xi source, one simple derivative factor at depth `d` carries
current-weighted charge at most

\[
{2h\over H_a^2}d,
\qquad H_a=b+h.
\]

Therefore every finite canonical Xi packet obeys

\[
\boxed{
\sum_{p'(c)=0}
\mathfrak q_{b,h}
\bigl((\operatorname{Im}c-H_0)_+\bigr)
\le
{2h\over H_a^2}
\mathfrak H_{H_0}(p).
}
\tag{T-105646.4}
\]

The aggregate current cost of all derivative crossings is controlled by one
parent upper-height moment.  No matching of individual zeros is required.

## 4. Interaction with the adaptive collar

For bandwidth `L`, split derivative factors into

```text
deep:      Im c-H_0 >= c/L;
shallow:   0<Im c-H_0<c/L.
```

Deep factors are source-visible by `T-105640`.  The shallow factors have total
penetration bounded by (T-105646.2), and their aggregate current-weighted cost
is bounded by (T-105646.4).

Thus the microscopic collar no longer consists of unstructured individual
crossings.  Its complete first height moment is inherited from the parent
packet and is monotone down the derivative ladder.

What remains topological is the possibility of many arbitrarily shallow
factors carrying small total depth but nonzero integer index.  The exact signed
source/index split of `L-105640--L-105643` is still required; a first-moment
bound alone cannot replace it.

## 5. Revised balanced gate

The conclusion-facing `BSTF105645` may now be sharpened to:

```text
BSTF105646 — depth-weighted balanced Turan flow

On cofinal Xi rectangles:

  use source contraction for factors deeper than c/L;
  use T-105646.4 for the aggregate weighted shallow source charge;
  retain only the integer signed model-space/endpoint index of the shallow
  collar;
  telescope the parent-minus-derivative Turan phase and one endpoint ledger.
```

The new theorem pays the **continuous weighted mass** of the collar
unconditionally at finite-packet scope.  The remaining RH-bearing object is
its integer/topological residue after cofinal endpoint transfer.

## 6. Exact status

```text
convex height majorization under differentiation    PROVED EXACT
all q>=1 upper-height moments decrease               PROVED EXACT
first-height derivative-ladder Lyapunov function     PROVED EXACT
aggregate derivative current charge from parent      PROVED EXACT / FINITE PACKET
deep adaptive source visibility                      PROVED EXACT
shallow integer signed index                         OPEN / RH-BEARING
cofinal Xi endpoint/canonical-product transfer        OPEN
POINTID105630                                        OPEN / RH-BEARING
BSTF105646                                           OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVEN
```

## 7. Scope

The theorem neither bounds the count of zero-depth factors nor proves that a
finite-packet inequality passes to Xi without endpoint terms.  Convex moment
majorization is compatible with many shallow critical points.  The integer
signed spectral flow and the physical denominator phase remain load bearing.
RH remains unproved.
