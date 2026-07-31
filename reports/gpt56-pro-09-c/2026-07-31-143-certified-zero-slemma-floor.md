# Certified-zero frame/S-lemma reduction of the visible low block

Agent: `gpt56-pro-09-c`  
Date: 2026-07-31  
Issues: #160 and #166  
Stacked base: PR #155 over PR #152

## Result

The zero-evaluation split of PR #159 left a direct finite positivity obligation
on the evaluation-visible block.  `L-14319` replaces that arbitrary matrix
problem by an exact one-parameter spectral dual.

After whitening a finite set of certified critical-line evaluations, the
visible set is

```text
<x,P_Z x> >= delta^2 ||x||^2,
```

where `P_Z` is the orthogonal projection onto the restricted exponential
representers at those zeros. The homogeneous S-lemma gives exactly

```text
visible floor
 = sup_(alpha>=0)
   lambda_min(A-alpha(P_Z-delta^2 I)).
```

A finite proof object therefore consists of one rational `alpha` and one PSD
matrix certificate.

## Block composition

Decomposing at the certified-zero representer space and applying the block
Temple--Schur theorem gives two scalar floors:

```text
gamma = complete complement floor,
b     = corrected zero-representer block floor.
```

The whole visible cone has floor

```text
b                                      if b<=gamma,
(1-delta^2) gamma + delta^2 b          if b>gamma.
```

This is an exact visibility-weighted interpolation.  A high-dimensional visible
packet no longer needs its own basis or principal-angle limit.

## Clark/model-space connection

The reduction is the finite unconditional shadow of the de Branges/model-space
picture: under RH the Weil Hilbert space is isomorphic to a de Branges space and
the zero kernels form the spectral/Clark coordinates of a self-adjoint
multiplication extension.  Burnol's Sonine-space results likewise connect zeta
zeros with complete and minimal kernel systems.  The present theorem does not
import RH from that picture; it uses only a finite proof-grade set of already
certified real zeros.

## Positive partial-zero frame

The Weil spectral formula shows that every certified real zero contributes an
exact positive rank-one evaluation form. Thus

```text
A_Weil = J_Z + A_residual.
```

A lower frame bound `J_Z>=sigma^2 G` and residual floor
`A_residual>=-epsilon G` prove the visible block floor `sigma^2-epsilon`.
This reverses the role of zero evaluations: they are not merely an obstruction
to radical approximation but an explicit positive component of the form.

## Exact control

`X-14312` uses only exact rational arithmetic. The retained model has global
minimum `-1` but visible floor `5/4`; eight mutation tests pass. The exact proof
object digest is

```text
746e5bb47be8bdd6b2ac16905f5027302638126a00e30dab2598c6ca6a862a18
```

## Remaining theorem

No RH proof is claimed. The residual form after extracting the certified-zero
frame still needs a cofinal lower bound. However, the load-bearing finite object
is now the small zero-representer Schur block plus one scalar multiplier, rather
than the full support-dependent visible packet.
