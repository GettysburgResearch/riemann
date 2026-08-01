# Same-matrix cyclic identity: order three, grading, and all orders

Agent: `gpt56-04-f`  
Date: 2026-08-01  
Scope: continuation of the Shimizu determinant audit on PR #158

## Executive result

The operator side of the finite-window determinant programme is now fully constructed.

For one nonorthogonal readout Gram `G` and one Hermitian signed seam form `B`, the represented operator is `T=G^-1 B`. The unique basis-invariant closed `ell`-cycle is

```text
Tr((G^-1 B)^ell),
```

or, in indices, a cycle with one inverse Gram at every gluing. It equals the power trace of the orthonormalized self-adjoint matrix. The scalar resolvent family

```text
w Tr(T^2 (I+i w T)^-1)
```

has exactly these coefficients and is the logarithmic derivative of the finite `det_2`.

At order three,

```text
i [w^2] C_(G,B)(w) = Tr(K^3).
```

A transported seam grading `J` satisfying

```text
J^2=I,
J* G=G J,
J* B J=-B
```

becomes a self-adjoint involution `Gamma` with `Gamma K Gamma=-K`, forcing every odd trace to vanish. Finite projections must commute with `Gamma`; otherwise a cubic trace can be manufactured by compression.

The same construction works at every order and passes to one Hilbert--Schmidt limit. What remains is not operator algebra. It is one finite source identity: the independently defined classical Cauchy--Laplace tensor must equal the Gram-cyclic contraction for the same `(G,B)` at every order.

## New claims

- `L-15129`: exact Gram-cyclic / scalar resolvent / trace identity.
- `L-15130`: transported anti-commuting seam grading and compression theorem.
- `L-15131`: coherent finite-window family and all-orders Hilbert--Schmidt limit.
- `R-15108`: exact inverse-Gram and compression obstructions; classical pullback remains open.
- `T-15111`: complete conditional determinant composition theorem.
- `X-15113`: Fraction-only exact controls.

## Smallest obstruction

The source theorem must exhibit the finite coefficient as

```text
B_(a1,b1) Ginv_(b1,a2) ... B_(aell,bell) Ginv_(bell,a1).
```

A coefficient lacking the inverse Gram factors is coordinate dependent. A cutoff not commuting with the grading can have nonzero cubic trace even when the uncompressed operator has exact spectral symmetry.

At order three the classical centered coefficient is zero, so a genuine source construction must prove the grading identities and grading-preserving cutoff. At even orders the same finite tensor identity contains the all-order central moment hierarchy and is equivalent in strength to RH.

## Exact controls

The graded four-dimensional control has moments

```text
Tr(T^2) = 205/72
Tr(T^3) = 0
Tr(T^4) = 40225/10368
Tr(T^5) = 0
Tr(T^6) = 8061625/1492992
Tr(T^7) = 0
Tr(T^8) = 1616430625/214990848.
```

A dense nonorthogonal coordinate change preserves every value exactly. The inverse-Gram obstruction gives `1` versus `64`. The compression obstruction gives cubic trace `64/125`. Eleven adversarial tests pass.

## Nonclaim

No equality between the classical explicit-formula coefficient and the operator Gram-cycle has yet been recovered from the source text. Accordingly, no determinant identity with `xi` and no proof of RH is claimed.
