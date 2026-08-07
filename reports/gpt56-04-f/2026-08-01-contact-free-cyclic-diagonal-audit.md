# Contact-free cyclic diagonal audit

**Date:** 2026-08-01  
**Agent:** `gpt56-04-f`  
**Branch:** `agent/gpt56-04-f/151-finsler-target-completion`  
**Status:** exact finite obstruction and necessary-and-sufficient replacement; **RH not proved**

## Executive outcome

The requested automatic identity

```text
one-contour scalar coefficient
=
connected product-contour cyclic coefficient
```

does not follow from the manuscript's displayed common linear finite-jet
subtraction, even after the Gram sewing, anti-commuting grading, finite
compression coherence, and Hilbert--Schmidt majorant have been supplied.

The first genuine even obstruction is order four.  Writing

```text
A = raw seam operator,
D = finite-jet counterterm seam operator,
K = A-D,
```

the connected coefficient is `Tr(K^4)`.  The one-contour subtraction removes
one linear coefficient `q_4`, while the product-contour contraction creates all
mixed closed loops containing `A` and `D`.

The exact quartic identity is

```text
Tr(A-D)^4
 = Tr(A^4)
   -4 Tr(A^3 D)
   +4 Tr(A^2 D^2)
   +2 Tr(A D A D)
   -4 Tr(A D^3)
   +Tr(D^4).
```

Thus, after a contact-free raw diagonal pullback, the finite-jet scalar must
satisfy the nonlinear Ward identity

```text
q_4
 = 4 Tr(A^3 D)
   -4 Tr(A^2 D^2)
   -2 Tr(A D A D)
   +4 Tr(A D^3)
   -Tr(D^4).
```

The phrase “the same counterterm is used in every ledger” establishes one-leg
consistency only.  It does not establish this connected quartic cumulant.

## Actual central-kernel coefficient

The manuscript fixes

```text
h_w(u)=(exp(wu)-1)/u
      =sum_(n>=1) w^n u^(n-1)/n!.
```

Because the cutoff and the finite-jet maps are linear, the displayed
one-contour finite-jet coefficient is

```text
q_(ell,M)
 =1/(ell-1)! * Z_M(C_M(chi_M u^(ell-2)), eta_M^fp).
```

In particular,

```text
q_(4,M)=1/6 * Z_M(C_M(chi_M u^2),eta_M^fp).
```

This is one linear contour pairing.  It is not the nonlinear quartic contact
polynomial above.  A universal identity on a scalar-stable class would force
both sides to vanish, because the one-contour term scales linearly with the
contour biform while the cyclic contact cumulant scales quartically.

## Exact graded obstruction

The retained rational model has

```text
A spectrum:  1,-1,2,-2
K spectrum:  11/5,-11/5,2/5,-2/5
D=A-K.
```

One exact grading anti-pairs every spectrum.  Hence all odd traces vanish.  The
quadratic moments also agree:

```text
Tr(A^2)=Tr(K^2)=10.
```

Nevertheless,

```text
Tr(A^4)=34,
Tr(K^4)=29314/625,
Tr(A^4)-Tr(K^4)=-8064/625.
```

The mixed contact traces are

```text
Tr(A^3D)  = 116/5
Tr(A^2D^2)= 584/25
Tr(AD^3)  = 1616/125
Tr(D^4)   = 10784/625.
```

A fixed linear one-contour counterterm can be zero on this datum, while the
required nonlinear Ward value is `-8064/625`.  Therefore exact grading,
quadratic matching, cubic parity, and one-leg counterterm invisibility do not
imply order-four contact cancellation.

## All-orders replacement

For a subset `S` of `{1,...,ell}`, let `W_S(A,D)` be the ordered word with `D`
at positions in `S` and `A` elsewhere.  Define

```text
P_ell(A,D)
 =sum_(empty != S subset [ell]) (-1)^|S| Tr W_S(A,D).
```

If `delta_ell^raw` is the raw one-contour/product-contour defect, then the
complete finite scalar/cyclic defect is

```text
Delta_ell^CL
 =delta_ell^raw-q_ell-P_ell(A,D).
```

Hence equality at all orders is equivalent to the finite-jet Ward hierarchy

```text
q_ell=delta_ell^raw-P_ell(A,D), ell>=2.
```

When the raw diagonal pullback is contact free this simplifies to

```text
q_ell=-P_ell(A,D).
```

This is necessary and sufficient.  Once it holds, the already proved
Hilbert--Schmidt geometric majorant applies without modification.

## Viable proof routes

There are only two structurally honest routes.

1. **Seam-radical finite jets.** Prove that the finite-jet range is annihilated
   on both seam legs and by the fixed scalar probe.  Then `D=0`, every mixed
   contact word vanishes, and every `q_ell=0`.
2. **Nonlinear Ward pullback.** Construct an additional nonlinear map from the
   order-`ell` central source to the connected cyclic tensor power and prove the
   exact Ward hierarchy for the fixed Riemann contour data.

The displayed linear finite-jet map supplies neither result.

## Files

- `L-15134-order-four-contact-polynomial-and-ward-hierarchy.md`
- `L-15135-central-kernel-jet-coefficients-and-degree-separation.md`
- `R-15111-common-finite-jet-subtraction-does-not-cancel-quartic-contacts.md`
- `T-15114-finite-jet-contact-ward-criterion.md`
- `X-15116-quartic-contact-ward/`

Nine exact mutation/adversarial tests pass.  The retained certificate digest is

```text
576630f9eb2aee928aab1701641c4cda5ffdf086c08f387f587b94e518e54479
```

## Proof boundary

No value of the actual Riemann quartic contact anomaly has been computed or
asserted.  The contribution proves that cancellation is additional nonlinear
data and supplies its exact necessary-and-sufficient formula.  Consequently
the determinant identity and RH remain unproved.