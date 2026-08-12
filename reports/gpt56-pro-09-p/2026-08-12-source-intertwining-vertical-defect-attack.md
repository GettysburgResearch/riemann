# Source-intertwining attack on the total vertical defect

Date: 2026-08-12  
Branch: `agent/gpt56-pro-09-i/198-square-screw-criterion`  
Scientific status: **RH remains unproved**

## Requested theorem

Construct a source-bound positive anisotropic metric for the Xi-like finite line, or prove directly

\[
 V_j
 =\sum_{\substack{\alpha:\ F_j(\alpha)=0\\\operatorname{Im}\alpha>0}}
   (\operatorname{Im}\alpha)^2
 \longrightarrow0.
\]

`T-19815` proves that this estimate, together with `L-19868`, would finish RH by a same-support vertical Darboux flattening and Hurwitz.

## Exact result of this pass

`L-19873` proves a new source-side bridge.  Let

```text
W_j = global arithmetic lift - finite zero extension,
D_j = W_j* W_j,
Q_j = D_j-lambda_j G_j >=0,
ker Q_j = C xi_j.
```

Let `A` be logarithmic differentiation and let `Lambda_j` be the finite real-frequency operator.  If

```text
A W_j-W_j Lambda_j = |g_j><eta_j| + R_j,
```

then, with `P_j=I-|xi_j><eta_j|`,

```text
Q_j T_j-T_j*Q_j
 =P_j*[
   R_j*W_j-W_j*R_j
   -lambda_j(G_j Lambda_j-Lambda_j G_j)
  ]P_j.
```

The rank-one Green boundary term disappears exactly.  No arbitrary positive metric is optimized.

Writing

```text
kappa_j=||W_j P_j Q_j^(-1/2)||,
rho_j=||R_j P_j Q_j^(-1/2)||_HS,
chi_j=||Q_j^(-1/2)P_j*(G_j Lambda_j-Lambda_j G_j)P_jQ_j^(-1/2)||_HS,
```

Schur triangularization gives

\[
 \boxed{
 V_j
 \le {1\over8}
      (2\kappa_j\rho_j+|\lambda_j|\chi_j)^2.}
\]

Thus the exact prime/source construction target is

```text
kappa_j=O(1),
rho_j ->0,
|lambda_j| chi_j ->0.
```

For an arithmetic lift `J_j`, the non-Green error is concretely

\[
 R_j=AJ_j-J_j\Lambda_j.
\]

This is a relative Hilbert--Schmidt derivative-intertwining theorem, not another free symmetrizer criterion.

## Why the current reservoir does not yet close it

The exterior-cardinal reservoir of `L-19862` is designed to give a constant residual-complement floor.  It does not estimate the derivative-intertwining norm.

Three natural repairs were tested.

### Long exact cardinals

A cardinal supported over many logarithmic cells can make the unnormalized error

```text
(A-d_k)J_k
```

small.  But narrowing each frequency packet destroys approximation of the broad Xi target unless the packets overlap at the critical Fourier spacing.  After division by the quotient floor, the resulting error is not known to vanish.

### Exact Xi derivative orbit

The derivatives

```text
r_Xi, A r_Xi, A^2 r_Xi, ...
```

are exact global arithmetic radicals and exactly lift the finite Krylov vectors

```text
p, Lambda p, Lambda^2 p, ... .
```

Using them makes the intertwining exact on that packet, but it also creates additional near-zero residual directions.  The one-line quotient floor then collapses.  Extending through the complete finite Krylov space moves the defect to the top polynomial boundary, where the centered bandwidth firewalls reappear.

### Isotropic complement

Making the complement Gram asymptotically scalar does not help.  `R-19850` shows that the normalized defect then retains the exact parity area between the odd scaling derivative and the even evaluation mismatch.

Therefore a successful construction must be simultaneously:

```text
anisotropic in the target/evaluation plane;
derivative-compatible in the intrinsic quotient metric;
source-bound before finite roots are inspected;
conditioned strongly enough that the relative HS error tends to zero.
```

No current theorem constructs such a section.

## Lower-semicontinuity boundary

If the finite transforms converge locally uniformly to `Xi` and `Xi` has an off-line zero `rho`, Hurwitz gives zeros `rho_j->rho`.  Consequently

\[
 \liminf_jV_j
 \ge |\operatorname{Im}\rho|^2.
\]

Combining this with `L-19873` proves that every proposed source section in a false-RH world has a nonvanishing normalized derivative-intertwining defect.  Increasing support, source precision, or the ordinary residual floor cannot remove it.

## Exact status

```text
source Green-commutator identity                 PROVED
source HS intertwining -> V_j bound              PROVED
complete moving-Hardy target convergence         PROVED (L-19868)
current exterior-cardinal relative intertwining  OPEN
source-bound anisotropic metric with V_j ->0      OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVEN
```

The new theorem turns the remaining task into a concrete prime/source estimate, but it does not establish that estimate.
