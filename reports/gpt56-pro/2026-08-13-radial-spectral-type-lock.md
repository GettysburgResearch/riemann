# Radical synthesis: diffuse radial source versus atomic zero depth

Date: 2026-08-13  
Branch: `research/gpt56-pro/91800-radial-spectral-type-lock`  
Parent: PR #428 at `76d849e3210fac73af2f6bf2eded91b29659a313`  
RH status: **unproved**

## Executive idea

The project had reduced the final route to a positive arithmetic-minus-model
kernel defect and a moving-node diagonal estimate.  The present pass changes
the proof object again.

Horizontal shift depth is treated as a spectral variable.

```text
arithmetic Julia source:
    innovations are born continuously in radial depth;

off-line zero pair:
    one positive hyperbolic port is born at one exact depth.
```

Thus the arithmetic source is diffuse while the RH obstruction is pure point.
If the completed source-to-model map is local for every radial interval and
positive before the intervals are summed, the hyperbolic output is absolutely
continuous with respect to a non-atomic source and must vanish.

This is a spectral-type argument, not a carrier-height estimate.

## Exact advances

### Prime radial density

The safe logarithmic Clark generator has the exact representation

\[
 \ell_{a,\sigma}(t)
 =\int_0^a
 2\sum_{p,k\ge1}
 (\log p)p^{-k(\sigma+2r)}
 (1-e^{-itk\log p})dr.
\]

Its polarized innovations form an absolutely continuous positive
operator-valued measure in `r`.

### Eta radial density

The full-carrier paired-eta detail is

\[
 K_{\sigma-\omega}^{\eta}
 -K_{\sigma+\omega}^{\eta}
 =\int_{-\omega}^{\omega}
 \left[
  \int_{\mathcal E}
  y e^{-(\sigma+r)y}e^{-i(t-s)y}dy
 \right]dr.
\]

Every radial density kernel is positive.

### Compact bridge

The dyadic/gamma compact bridge has the finite-interval refinement

\[
 F_L(q-\omega)-F_L(q+\omega)
 =\int_{-\omega}^{\omega}
  \int_0^L t e^{-(q+r)t}dt\,dr.
\]

The old free pole contributes no positive-depth source atom.

### Hyperbolic depth measure

An off-line zero coordinate `zeta=x+iy` contributes the positive atom

\[
 m_\zeta\mathsf H_\zeta\,\delta_x(dr)
\]

and, at one node,

\[
 m_\zeta
 \log\frac{(\eta+x)^2+y^2}{(\eta-x)^2+y^2}
 \delta_x(dr).
\]

The complete crossed-zero port is pure point in horizontal depth.

### Spectral-type theorem

If positive operator-valued measures satisfy

\[
 \mathsf A
 =\mathsf C+\mathsf S+\mathsf H+\mathsf E
\]

interval by interval and `A` is diffuse, then `H` is absolutely continuous
with respect to `A`.  A pure-point `H` must therefore vanish.

The product-system version says that an interval-natural Fock morphism is an
`L^infinity(dr)`-module map and cannot create a target atom absent from the
source spectral measure.

## The new conclusion-producing theorem

**Radially Local Source Lock (RLSL).**  Prove the completed positive source and
model identity on every radial Borel interval before summing the horizontal
shift generations:

\[
 \mathsf A^{\rm arith}(I)
 =\mathsf C^{\rm crit}(I)
  +\mathsf S^{\rm st}(I)
  +\mathsf H^{\rm hyp}(I)
  +\mathsf E^{\rm aux}(I).
\]

Then the pure-point hyperbolic measure is zero and RH follows.

An approximate form suffices: on shrinking intervals around a proposed depth,
the local source norm and locality error need only tend to zero.

## Why this may be a better gate

The parent route required:

```text
one global kernel PSD theorem;
one o(Y^-2) large-node estimate.
```

RLSL instead requires:

```text
coefficient-one locality under arbitrary radial refinement.
```

That locality is already native to the source:

```text
prime births occur over dr;
eta details occur over dr;
bridge details occur over dr;
gamma sections can be split over arbitrary radial partitions.
```

The main uncertainty is whether the completed critical/stable model map can be
made natural for the same continuous product system.  A global isometry is not
enough; it may rotate diffuse source mass into an atomic depth port.

## Hostile firewall

A total positive equality can hide an atom:

```text
source total = 1;
critical total = 0.7;
hyperbolic atom total = 0.3.
```

One fixed dyadic grid is also insufficient, because an atom can hide inside a
cell.  The proof must use all rational intervals, all translated dyadic grids,
or an explicit module relation.

## Verification

Retained verdict:

```text
PASS_RADIAL_SPECTRAL_TYPE_LOCK
```

Selected controls:

```text
prime radial identity error       5.27e-82
eta radial identity error         1.96e-81
finite-grid atom spectral gap     3.1597e-3
shrinking diffuse norm bound      0.4472 -> 0.06325
```

The replay verifies finite identities and the abstract firewall.  It does not
prove the full gamma continuous product, RLSL, or RH.

## Current ranking

1. **RLSL / radial spectral type.**  Most structurally decisive; no height
   asymptotic if interval locality can be proved.
2. **Parent kernel lock.**  Strong fallback: global PSD plus `o(Y^-2)`.
3. **Full Clark–Redheffer CPPD.**  Retains every packet cross term but carries
   the heaviest operator burden.

## Exact boundary

```text
prime/eta/bridge diffuse radial sources          EXACT
gamma continuous radial assembly                 PROPOSED / REVIEW REQUIRED
crossed-zero depth measure                       PURE POINT EXACT
spectral-type exclusion                          EXACT ABSTRACT THEOREM
interval-natural Fock morphism exclusion          EXACT
radially local completed source/model lock        OPEN / RH-EQUIVALENT
Riemann Hypothesis                               UNPROVED
```
