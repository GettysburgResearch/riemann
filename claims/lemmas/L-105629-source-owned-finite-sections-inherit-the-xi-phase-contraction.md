# L-105629 — Every source-owned finite section inherits the safe-region base-Xi contraction

Claim ID: `L-105629`  
Status: **PROVED EXACT FINITE-COMPRESSION THEOREM**  
Created: 2026-08-25  
Depends on: `L-105628`  
RH status: **not assumed**

## 1. Abstract compression

Let `H` be a Hilbert space and suppose

\[
V^*RV\preceq R
\tag{L-105629.1}
\]

for a bounded positive operator `R` and an isometry `V`.

Let

\[
W:\mathbb C^d\to H
\]

be any isometry. Compressing (L-105629.1) gives

\[
\boxed{
W^*V^*RVW\preceq W^*RW.
}
\tag{L-105629.2}
\]

No commutation between `W`, `V` and `R` is required.

More generally, if `W` is merely injective, put

\[
G=W^*RW.
\]

On the support of `G`, the normalized finite operator

\[
\boxed{
K_G
=G^{-1/2}W^*V^*RVWG^{-1/2}
}
\tag{L-105629.3}
\]

satisfies

\[
\boxed{0\preceq K_G\preceq I.}
\tag{L-105629.4}
\]

Thus exact source normalization is automatically contractive on every finite
source-owned frame.

## 2. Tapers and nested sections

Let `P` be any orthogonal projection in `H`. Taking `W` to be an isometric
coordinate map onto `P H` gives

\[
\boxed{
PV^*RVP\preceq PRP
\quad\text{on }PH.
}
\tag{L-105629.5}
\]

If `A` is any bounded observation operator, apply (L-105629.2) to the polar
isometry in `R^(1/2)A`. Equivalently, every frame formed **after** the positive
source metric is installed inherits the contraction.

Consequently:

```text
finite frequency cutoff;
dyadic source partition;
source-owned smooth taper;
finite-dimensional source basis;
nested source Gram section
```

introduce no adverse phase-collision term by themselves.

## 3. Safe-region base-Xi specialization

Fix

\[
b\ge\beta_0,
\qquad h>0,
\qquad H=b+h.
\]

`L-105628` proves

\[
V_H^*M_{r_{b,h}}V_H
\preceq M_{r_{b,h}}.
\]

For every finite source-owned embedding `W_T`,

\[
\boxed{
W_T^*V_H^*M_{r_{b,h}}V_HW_T
\preceq
W_T^*M_{r_{b,h}}W_T.
}
\tag{L-105629.6}
\]

After whitening by the exact finite current Gram, the actual base-Xi
all-pass/Turan source has operator norm at most one throughout the safe region.

This removes the following items from the intrinsic phase ledger whenever the
frame is constructed in the source metric:

```text
finite source cutoff;
source taper;
finite source basis;
source Gram whitening;
projection of the causal all-pass.
```

## 4. The remaining finite and descent interfaces

A physical zero-count/companion frame need not be source-owned. The finite
interface is:

```text
BANKID105629

Represent the actual cofinal base-Xi zero-count observation space as a
source-owned finite section W_T up to a controlled finite codimension and one
telescoping endpoint charge.
```

If `BANKID105629` is exact, (L-105629.6) gives the finite safe-region phase
contraction without further source estimates. If it is approximate, the scalar
Frobenius/trace defects of sibling `ROBUSTFRAME106400` measure precisely the
failure of the physical bank to be this source-owned section.

Even an exact bank identification does not descend below `beta_0`; that is the
separate `SAFEDESC105628` obstruction. Thus the pointwise RH route needs both:

```text
finite bank/index identification;
continuation of the safe contraction through the first descending base.
```

## 5. Scope

The theorem does not prove `BANKID105629` or `SAFEDESC105628`. Multiplication
by an arbitrary physical cutoff **before** source normalization is not asserted
to be source-owned. Endpoint winding and denominator-zero codimension are not
removed. Higher derivative rungs require separate source profiles. RH remains
unproved.
