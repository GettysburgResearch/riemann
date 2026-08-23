# M-105330 — Hostile review contract for the dual Vandermonde contour hierarchy

Claim ID: `M-105330`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
RH status: **unproved**

## Frozen source context

```text
PR #729 preimage head: 4c3c3b8b0c7b70e7596b3345b1ac1ce37a464fac
parent PR #724 head:   452978883b0009f002cfec426dfd5eb10041a15c
related PR #726 head:  b4c3ecff7a8616498348a67d9977b3f56db47e33
fixed-order PR #720:   0e27e486adfb0a44c73bedebe26d678d4ce09a1c
```

The complete source-lock object is
`integration/2026-08-23/t105330-source-lock.json`.

## Required review order

1. Verify the signs in the two moments of `L-105328.2`.
2. Reconstruct `mathsf P=V^T diag(-rho)V` and `mathsf G=V^T V`.
3. Verify that a nonreal conjugate critical pair contributes a hyperbolic
   block; positive leading minors must not be claimed without excluding it.
4. Check the pencil orientation:
   `det(mathsf P+t mathsf G)/det(mathsf G)=prod(t-rho_c)`.
5. Verify the factor `(-1)^k/k!` in the critical multiple-contour determinant.
6. Replay the quartic separator. Both first determinants must be positive and
   the full third determinant negative.
7. Check the boundary contour-square identity and the squared Cauchy
   determinant denominator.
8. Keep the confluent one-centre hierarchy only as a necessary consequence;
   do not promote it to the separated all-packet theorem.
9. Review `T-105330` only as a conditional Xi conclusion graph.

## Binding signs

```text
rho_c = F(c)/F''(c)
critical positive weight = -rho_c
wrong real extremum = rho_c > 0 = one negative critical pivot
```

The count matrix uses `F''/F'`, whose residue at every simple critical point is
`+1`. Reversing either convention reverses the pencil and invalidates the
resultant comparison.

## Exact scope versus open Xi use

The following are finite-window identities:

- Vandermonde factorization;
- generalized residue characteristic polynomial;
- Cauchy–Binet/Andreief determinant expansions;
- equivalence of complete critical positivity to real negative residues;
- equivalence of every boundary packet determinant to the boundary-PSD component of BRP.

They do **not** prove:

- any favorable fixed-low-order Xi determinant;
- the moving-saddle theorem;
- a cofinal regular exhaustion;
- common-zero or multiplicity exclusion;
- RH.

## Replay contract

```bash
python -B experiments/X-105330-dual-vandermonde-contour-hierarchies/verify.py \
  --output experiments/X-105330-dual-vandermonde-contour-hierarchies/results/verification.json
```

Expected:

```text
PASS_X_105330_DUAL_VANDERMONDE_CONTOUR_HIERARCHIES
222 exact rational checks
93f59673fad499278a27b6a93f801d96156907759642bf6b8fc9fb0626a66c5e
```

## Binding scientific boundary

```text
finite dual determinant identities       PROVED EXACT / REVIEW REQUIRED
CRVH105330                                OPEN
BCVH105330                                OPEN
PRES105220                                OPEN
BRP105220                                 OPEN
Riemann Hypothesis                        UNPROVED
```
