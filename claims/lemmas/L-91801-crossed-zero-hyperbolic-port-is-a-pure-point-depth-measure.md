# L-91801 — The crossed-zero hyperbolic port is a pure-point measure in horizontal depth

Claim ID: `L-91801`  
Status: **PROVED EXACT MODEL-SIDE DEPTH SPECTRAL DECOMPOSITION**  
Created: 2026-08-13  
Depends on: `L-91313`, `L-91420`, `L-91520/L-91620`  
RH status: **unproved**

## 1. Depth grading of an off-line zero

Use the centered zero coordinate

\[
 \zeta=x+iy,
 \qquad
 x=\left|\Re\rho-\frac12\right|\in(0,1/2).
\]

The number `x` is the horizontal depth of the reflected off-line pair.  For a
horizontal threshold `a>0`, the pair belongs to the crossed-zero Blaschke
factor exactly when

\[
 a<x.
\]

Thus every off-line pair has one birth depth and persists through all finer
thresholds.

## 2. One-zero kernel atom

Let

\[
 b_\zeta(z)=\frac{z-\zeta}{z+\overline\zeta}
\]

be the right-half-plane Blaschke factor.  Its positive de
Branges--Rovnyak kernel is

\[
\boxed{
 \mathsf H_\zeta(z,w)
 =\frac{1-b_\zeta(z)\overline{b_\zeta(w)}}
        {z+\overline w}
 \succeq0.
}
\tag{L-91801.1}
\]

For multiplicity `m_zeta`, attach the operator-valued atom

\[
\boxed{
 d\mathsf H_\zeta(r)
 =m_\zeta\mathsf H_\zeta\,\delta_x(dr).
}
\tag{L-91801.2}
\]

For a finite packet of test nodes this is a positive matrix-valued point mass.

## 3. Complete hyperbolic depth measure

Summing over reflected off-line pairs gives

\[
\boxed{
 d\mathsf H^{\rm hyp}(r)
 =\sum_{\zeta:\Re\zeta>0}
  m_\zeta\mathsf H_\zeta\,\delta_{\Re\zeta}(dr).
}
\tag{L-91801.3}
\]

On every compact depth interval bounded away from zero and every finite
carrier packet, the sum is locally finite after the standard height
localization.  Cofinal height limits are taken in the same monotone sense as
in the annular Blaschke products.

For a Borel interval `I`,

\[
\boxed{
 \mathsf H^{\rm hyp}(I)
 =\sum_{\Re\zeta\in I}
  m_\zeta\mathsf H_\zeta.
}
\tag{L-91801.4}
\]

This is precisely the hyperbolic port created by the zeros whose depths lie in
`I`.

## 4. One-node scalarization

At a fixed interior node `eta>0`, the atom has mass

\[
\boxed{
 g_\eta(\zeta)
 =-\log|b_\zeta(\eta)|^2
 =\log\frac{(\eta+x)^2+y^2}
              {(\eta-x)^2+y^2}>0.
}
\tag{L-91801.5}
\]

Hence the logarithmic depth measure is

\[
\boxed{
 d\Lambda_\eta^{\rm hyp}(r)
 =\sum_\zeta
  m_\zeta g_\eta(\zeta)\,\delta_{\Re\zeta}(dr).
}
\tag{L-91801.6}
\]

For an annulus `(a,b]`,

\[
 \Lambda_\eta^{\rm hyp}((a,b])
 =\Lambda_{a,b}^{\rm ann}(\eta)
\]

from `L-91520/L-91620`.

## 5. The depth operator

Let

\[
 \mathcal H_{\rm hyp}
 =\bigoplus_{\zeta:\Re\zeta>0}
  \mathcal H_\zeta
\]

be the direct sum of the positive crossed-zero ports.  Define the self-adjoint
depth operator

\[
\boxed{
 D_{\rm hyp}|_{\mathcal H_\zeta}
 =(\Re\zeta)I.
}
\tag{L-91801.7}
\]

Its spectral measure is exactly (L-91801.3).  In particular, the positive-depth
hyperbolic channel is pure point.

Critical-line zeros occur at depth zero and belong to the boundary spectral
subspace.  They are not part of (L-91801.3).

## 6. RH as absence of positive-depth atoms

The following statements are equivalent:

```text
RH;
D_hyp has no spectrum in (0,1/2);
H_hyp({r})=0 for every r>0;
Lambda_eta^hyp has no positive-depth atom for one (hence every) eta>0.
```

The equivalence uses only positivity of every one-zero charge and functional
equation symmetry.

## 7. Exact boundary

```text
off-line pair -> one positive depth atom       EXACT
full hyperbolic port -> pure-point OVM          EXACT
one-node log charge                             EXACT POSITIVE
critical-line channel                           BOUNDARY DEPTH ZERO
RH -> no positive-depth atom                    EXACT EQUIVALENCE
arithmetic domination of the depth OVM          OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
