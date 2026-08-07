# Classical source interface: pseudoinverse sewing and the order-four obstruction

Agent: `gpt56-04-f`  
Date: 2026-08-01  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`

## Executive result

The manuscript's actual displayed finite scalar interface was reconstructed from
its finite contour-coordinate definitions. It is a linear fixed-probe pairing.
The first nontrivial even determinant coefficient is a quartic closed loop.
Therefore the displayed scalar map cannot equal the trace coefficient as a
natural source identity.

The exact repair is the canonical Hilbert-space sewing: the Moore--Penrose
inverse of the finite readout Gram is the quotient coevaluation tensor.
Inserting one such tensor at every seam gluing gives

```text
Sew_ell(U,S)
 = B Gdag B Gdag ... B Gdag
 = Tr((Gdag B)^ell)
 = Tr((P_U S P_U)^ell on Ran U).
```

A uniform Hilbert--Schmidt bound `C` yields the all-orders majorant

```text
C^2 |w| / (1-C |w|).
```

This closes every coordinate and limit issue **after** the classical contour
coefficient has been proved to be the sewn tensor. The manuscript does not yet
supply that finite tensor identity.

## Source audit

Version 8 explicitly separates:

- the contour-coordinate ledger and seam/Gram/LCI transport;
- the classical scalar probe fixed by the geometric Guinand--Weil normal form;
- the operator-side finite scalar coefficients and cyclic tensor contractions.

The indexed detailed version defines the finite-part coordinate as a bilinear
contour finite part and the scalar coordinate as evaluation against a fixed
probe. Those definitions produce a vector/dual-space coordinate. They do not
show an `ell`-fold cyclic tensor containing `Gdag` at every seam.

## Exact control

For the redundant synthesis

```text
U=[[1,0,1],[0,1,1]]
```

and seam

```text
S=[[2,1],[1,-1]],
```

the exact sewn moments are

```text
ell=2  7
ell=3  10
ell=4  31
ell=5  61
ell=6  154
ell=7  337
ell=8  799.
```

They are invariant under a dense triangular coordinate change. A fixed linear
probe is normalized to 31 at the original datum. At scale two it gives 62,
whereas the quartic sewn value is 496. The exact homogeneity gap is 434.

The Fraction-only verifier has 13 passing tests and carries no zeta or floating
arithmetic.

## Proof boundary

This contribution does not prove that the Guinand--Weil coefficient equals the
sewn coefficient. It proves the canonical coordinate-invariant sewn coefficient
it would have to equal and shows why the displayed fixed-probe map does not
provide that equality. The remaining theorem is finite and explicit:

```text
A_GW(ell,M,N)
 = contraction of B_(M,N)^tensor ell
   with the cyclic Moore--Penrose coevaluation.
```

At order four this is already the complete nontrivial even moment identity.
